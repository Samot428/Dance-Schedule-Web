from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import UploadedScheduleFile

# Create your views here.
def calendar_view(request):
    return redirect('main:calendar_view')

@ensure_csrf_cookie
def schedule_view(request):
    return render(request, 'schedule_view.html')

def upload_schedule_files(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=400)

    files = request.FILES.getlist('files') or []
    if not files:
        return JsonResponse({'status': 'error', 'message': 'No files provided'}, status=400)

    uploaded_files_info = []
    for f in files:
        uploaded_file = UploadedScheduleFile.objects.create(
            filename=f.name,
            file=f,
        )
        uploaded_files_info.append({
            'id': uploaded_file.id,
            'filename': uploaded_file.filename,
            'size': uploaded_file.file.size,
            'uploaded_at': uploaded_file.uploaded_at.strftime('%Y-%m-%d %H:%M'),
            'url': uploaded_file.file.url,  # useful for preview/download
        })

    return JsonResponse({'status': 'success', 'files': uploaded_files_info})

def get_uploaded_files(request):
    files = UploadedScheduleFile.objects.all().order_by('-uploaded_at')
    files_data = [{
        'id': f.id,
        'filename': f.filename,
        'size': f.file.size,
        'uploaded_at': f.uploaded_at.strftime('%Y-%m-%d %H:%M'),
        'url': f.file.url,
    } for f in files]
    return JsonResponse({'files': files_data})

from django.views.decorators.csrf import csrf_exempt

def delete_uploaded_file(request, file_id):
    if request.method not in ('DELETE', 'POST'):
        return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=400)

    try:
        f = UploadedScheduleFile.objects.get(id=file_id)
    except UploadedScheduleFile.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'File not found'}, status=404)

    f.file.delete(save=False)
    f.delete()
    return JsonResponse({'status': 'success'})