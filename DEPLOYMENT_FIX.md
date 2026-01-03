# 🔧 Quick Fix for Render Deployment Issue

## Problem
Build fails with `ModuleNotFoundError: No module named 'DANCE_CALENDAR_WEB'`

## Solution
I've updated the build script to fix the Python path issue. Follow these steps:

### 1. Commit and Push Changes
```bash
git add .
git commit -m "Fix: Update build script for Render deployment"
git push origin main
```

### 2. Render Will Auto-Redeploy
Once you push, Render will automatically detect the changes and redeploy.

### 3. Alternative: Manual Redeploy
If auto-deploy isn't working:
- Go to your Render dashboard
- Click on your service
- Click "Manual Deploy" → "Clear build cache & deploy"

---

## What Was Fixed

✅ **Updated `build.sh`:**
- Added `PYTHONPATH` export to include Django project directory
- Ensures Django can find the settings module

✅ **Updated `render.yaml`:**
- Added `PYTHONPATH` environment variable
- Fixed `startCommand` to include port binding

✅ **Created `build_alt.sh`:**
- Alternative simpler build script if first one fails

---

## If Build Still Fails

### Try Alternative Build Script

In Render dashboard:
1. Go to your service settings
2. Change **Build Command** to: `bash build_alt.sh`
3. Click "Save Changes"
4. Trigger manual deploy

### Or Use This Minimal Config

**Build Command:**
```bash
pip install -r requirements.txt && python DANCE_CALENDAR_WEB/manage.py collectstatic --no-input && python DANCE_CALENDAR_WEB/manage.py migrate
```

**Start Command:**
```bash
cd DANCE_CALENDAR_WEB && gunicorn DANCE_CALENDAR_WEB.wsgi:application --bind 0.0.0.0:$PORT
```

---

## Environment Variables Checklist

Make sure these are set in Render:

✅ `DEBUG` = `False`
✅ `SECRET_KEY` = (auto-generated or your own)
✅ `ALLOWED_HOSTS` = `.onrender.com`
✅ `DATABASE_URL` = (connected to your PostgreSQL)
✅ `PYTHON_VERSION` = `3.11.0`
✅ `PYTHONPATH` = `/opt/render/project/src/DANCE_CALENDAR_WEB`

---

## After Successful Deploy

Create superuser via Render Shell:
```bash
cd DANCE_CALENDAR_WEB
python manage.py createsuperuser
```

Then access your site at: `https://dance-calendar-web.onrender.com/admin`

---

## Still Having Issues?

Check the build logs:
- Look for Python path errors
- Verify all dependencies installed
- Check database connection

Contact me with the full error log if needed!
