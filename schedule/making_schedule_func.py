from collections import defaultdict
from datetime import time

def convert_to_min(time_obj):
    """Converts time(8, 20) to minutes"""
    h = time_obj.hour
    m = time_obj.minute

    minutes = h*60 + m
    return minutes

def min_to_time_str(minutes):
    """Converts minutes to time string HH:MM"""
    h = minutes // 60
    m = minutes % 60
    return f"{h:02d}:{m:02d}"
    
def make_trainers_windows(trainers, day):
    from main.models import TrainerDayAvailability
    trainers_windows = {}
    for trainer in trainers:
        tda = TrainerDayAvailability.objects.get(trainer=trainer, day=day)
        st = convert_to_min(tda.start_time)
        et = convert_to_min(tda.end_time)
        group_lessons = []
        try:
            for gl in trainer.group_lesson.all():
                x = gl.__str__().split("-")
                stg = convert_to_min(time(int(x[0].split(":")[0]), int(x[0].split(":")[1])))
                etg = convert_to_min(time(int(x[1].split(":")[0]), int(x[1].split(":")[1])))
                group_lessons.append((stg, etg))
        except:
            pass
        
        # Create time windows for this trainer
        time_windows = []
        for i in range(st, et, 5):
            time_str = min_to_time_str(i)
            is_available = True
            
            # Check if this time slot falls within any group lesson
            if group_lessons:
                for gl_start, gl_end in group_lessons:
                    if gl_start <= i < gl_end:
                        is_available = False
                        break
            
            time_windows.append((time_str, is_available))
            
        trainers_windows[trainer] = time_windows
            
    return trainers_windows

def sort_couples_by_class(couples):
    classes = ['A', 'B', 'C', 'D', 'E']
    sorted_couples_lat = defaultdict(list)
    sorted_couples_stt = defaultdict(list)
    for couple in couples:
        name, dance_class_lat, dance_class_stt = couple.name, couple.dance_class_lat, couple.dance_class_stt
        sorted_couples_lat[dance_class_lat].append(couple)
        sorted_couples_stt[dance_class_stt].append(couple)
    
    return sorted_couples_lat, sorted_couples_stt

def sort_couples_by_group(couples, groups):
    """Sort couples by their group's index."""
    sorted_groups = sorted(groups, key=lambda g: g.index)

    # Starts with the non group couples 
    sorted_couples = [c for c in couples if c.group is None]
    for group in sorted_groups:
        group_couples = [c for c in couples if c.group == group]
        sorted_couples.extend(group_couples)
    return sorted_couples

def match_couples_availability(day_dancers_avail, day_times):
    couples_availability = {}

    return couples_availability

def create_schedule(cawt, trainers_windows, couples):
    """Create a schedule for one day.

    Args:
        cawt: dict mapping couple name -> list of (time_str, is_available) slots (typically coarse, e.g., 30-min)
        trainers_windows: dict mapping Trainer -> list of 5-min (time_str, is_available)
        couples: ordered list of Couple objects to schedule
    """

    # Precompute availability intervals per couple so we can block any overlap, not just matching exact timestamps.
    couple_intervals = {}
    for name, slots in cawt.items():
        if not slots:
            continue
        # Infer slot length from consecutive entries (fallback to 30 minutes).
        slot_lengths = []
        for i in range(len(slots) - 1):
            h1, m1 = map(int, slots[i][0].split(':'))
            h2, m2 = map(int, slots[i + 1][0].split(':'))
            diff = (h2 * 60 + m2) - (h1 * 60 + m1)
            if diff > 0:
                slot_lengths.append(diff)
        default_slot = min(slot_lengths) if slot_lengths else 30

        intervals = []
        for i, (time_str, avail) in enumerate(slots):
            h, m = map(int, time_str.split(':'))
            start = h * 60 + m
            if i + 1 < len(slots):
                h2, m2 = map(int, slots[i + 1][0].split(':'))
                end = h2 * 60 + m2
            else:
                end = start + default_slot
            intervals.append((start, end, avail))
        couple_intervals[name] = intervals

    solution = {}

    def backtrack(idx = 0):
        if idx == len(couples):
            return True
        p = couples[idx]
        name = p.name
        lesson_time = p.min_duration
        for trainer in trainers_windows:
            # time slots
            ts = trainers_windows[trainer]

            for i, (time_str, is_available) in enumerate(ts):
                if not is_available:
                    continue

                # convert time_tr to minutes
                h, m = map(int, time_str.split(':'))
                start_min = h * 60 + m
                end_min = start_min + lesson_time

                # Check whether couple is available for the entire lesson interval.
                couple_available = True
                intervals = couple_intervals.get(name, [])
                for slot_start, slot_end, avail in intervals:
                    overlap = not (slot_end <= start_min or slot_start >= end_min)
                    if overlap and not avail:
                        couple_available = False
                        break
                if not couple_available:
                    continue

                # Check if all trainer slots in this time range are available
                can_schedule = True
                slots_to_mark = []

                # Calculate how many 5-minutes are needed
                num_slots = (lesson_time + 4) // 5 # Round up

                for j in range(i, min(i + num_slots, len(ts))):
                    t_str, t_avail = ts[j]
                    if not t_avail:
                        can_schedule = False
                        break
                    slots_to_mark.append(j)
                
                if not can_schedule:
                    continue

                # Mark slots as unavailable
                for j in slots_to_mark:
                    ts[j] = (ts[j][0], False)
                    
                solution[p] = (trainer, time_str)

                # Recurse to next couple
                if backtrack(idx + 1):
                    return True

                # Backtrack: undo changes
                del solution[p]
                for j in slots_to_mark:
                    ts[j] = (ts[j][0], True)
        return False

    # Start the backtrack 
    backtrack(0)
    return solution