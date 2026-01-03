# 🚀 Deployment Guide - Dance Calendar Web

This guide will help you deploy your Django Dance Calendar application to the cloud for FREE!

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Prepare for Deployment](#prepare-for-deployment)
3. [Deploy to Render.com](#deploy-to-rendercom-recommended)
4. [Deploy to PythonAnywhere](#deploy-to-pythonanywhere-alternative)
5. [Deploy to Railway](#deploy-to-railway-alternative)
6. [Post-Deployment Steps](#post-deployment-steps)
7. [Troubleshooting](#troubleshooting)

---

## ✅ Prerequisites

- Git installed on your computer
- GitHub account (free)
- Your project code ready

---

## 🛠 Prepare for Deployment

### 1. Initialize Git Repository (if not already done)

```bash
cd d:\python\Dance_Calendar_Web
git init
git add .
git commit -m "Initial commit - Dance Calendar Web"
```

### 2. Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository (name it `dance-calendar-web`)
3. **DO NOT** initialize with README (you already have code)
4. Copy the repository URL

### 3. Push to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/dance-calendar-web.git
git branch -M main
git push -u origin main
```

---

## 🌐 Deploy to Render.com (Recommended)

### Why Render?
- ✅ Always FREE tier available
- ✅ Free PostgreSQL database
- ✅ Auto-deploy from GitHub
- ✅ Free SSL/HTTPS
- ⚠️ Sleeps after 15 min inactivity (wakes up in ~30 seconds)

### Step-by-Step Instructions:

1. **Go to Render.com**
   - Visit https://render.com
   - Sign up with GitHub

2. **Connect Your Repository**
   - Click "New +" → "Web Service"
   - Connect your GitHub account
   - Select `dance-calendar-web` repository

3. **Configure Web Service**
   - **Name:** `dance-calendar-web`
   - **Region:** Choose closest to you
   - **Branch:** `main`
   - **Root Directory:** Leave empty
   - **Runtime:** `Python 3`
   - **Build Command:** `bash build.sh`
   - **Start Command:** `cd DANCE_CALENDAR_WEB && gunicorn DANCE_CALENDAR_WEB.wsgi:application`
   - **Plan:** FREE

4. **Add Environment Variables**
   Click "Advanced" → Add environment variables:
   ```
   DEBUG=False
   SECRET_KEY=<click Generate to create secure key>
   ALLOWED_HOSTS=.onrender.com
   PYTHON_VERSION=3.11.0
   ```

5. **Create PostgreSQL Database**
   - Go back to Dashboard
   - Click "New +" → "PostgreSQL"
   - **Name:** `dance-calendar-db`
   - **Plan:** FREE
   - Click "Create Database"
   - Wait for it to provision

6. **Connect Database to Web Service**
   - Go to your web service settings
   - Click "Environment"
   - Add new variable:
     ```
     DATABASE_URL=<copy from your PostgreSQL database internal connection string>
     ```

7. **Deploy!**
   - Click "Create Web Service"
   - Wait 5-10 minutes for first deployment
   - Your app will be live at: `https://dance-calendar-web.onrender.com`

---

## 🐍 Deploy to PythonAnywhere (Alternative)

### Why PythonAnywhere?
- ✅ Always FREE and online (no sleeping)
- ✅ Very beginner-friendly
- ✅ No credit card required
- ⚠️ Limited CPU (100 seconds/day on free tier)
- ⚠️ Manual updates (no auto-deploy)

### Step-by-Step Instructions:

1. **Sign Up**
   - Go to https://www.pythonanywhere.com
   - Create a free "Beginner" account

2. **Upload Your Code**
   - Open a Bash console
   - Clone your repository:
     ```bash
     git clone https://github.com/YOUR_USERNAME/dance-calendar-web.git
     cd dance-calendar-web
     ```

3. **Create Virtual Environment**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.11 myenv
   pip install -r requirements.txt
   ```

4. **Set Up Web App**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Manual configuration"
   - Select Python 3.11

5. **Configure WSGI File**
   - Click on WSGI configuration file link
   - Replace contents with:
   ```python
   import os
   import sys
   
   path = '/home/YOUR_USERNAME/dance-calendar-web/DANCE_CALENDAR_WEB'
   if path not in sys.path:
       sys.path.append(path)
   
   os.environ['DJANGO_SETTINGS_MODULE'] = 'DANCE_CALENDAR_WEB.settings'
   
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

6. **Set Environment Variables**
   - In Web tab, scroll to "Environment variables"
   - Add:
     ```
     DEBUG=False
     SECRET_KEY=your-secret-key-here
     ALLOWED_HOSTS=your-username.pythonanywhere.com
     ```

7. **Run Migrations**
   ```bash
   cd dance-calendar-web/DANCE_CALENDAR_WEB
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```

8. **Reload Web App**
   - Click green "Reload" button
   - Visit: `https://your-username.pythonanywhere.com`

---

## 🚂 Deploy to Railway (Alternative)

### Why Railway?
- ✅ $5 free credit/month
- ✅ Very easy deployment
- ✅ Auto-deploy from GitHub
- ⚠️ Credit runs out with heavy usage

### Step-by-Step Instructions:

1. **Sign Up**
   - Go to https://railway.app
   - Sign up with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose `dance-calendar-web`

3. **Add PostgreSQL**
   - Click "New"
   - Select "Database" → "PostgreSQL"

4. **Configure Environment Variables**
   - Click on your web service
   - Go to "Variables" tab
   - Add:
     ```
     DEBUG=False
     SECRET_KEY=<generate secure key>
     ALLOWED_HOSTS=.railway.app
     DATABASE_URL=${{Postgres.DATABASE_URL}}
     ```

5. **Deploy**
   - Railway automatically detects Django
   - It will deploy using your Procfile
   - Visit your generated URL

---

## 📝 Post-Deployment Steps

### 1. Create Superuser (Admin Account)

**For Render/Railway:**
```bash
# Use their web CLI/console
python manage.py createsuperuser
```

**For PythonAnywhere:**
```bash
cd ~/dance-calendar-web/DANCE_CALENDAR_WEB
python manage.py createsuperuser
```

### 2. Access Admin Panel

Visit: `https://your-domain.com/admin`

### 3. Configure Your Site

1. Log in to admin
2. Add Groups
3. Add Dancers
4. Add Trainers
5. Create Days

---

## 🔧 Troubleshooting

### Issue: "DisallowedHost" Error

**Solution:** Add your domain to ALLOWED_HOSTS
- Update environment variable: `ALLOWED_HOSTS=yourdomain.com,.onrender.com`

### Issue: Static Files Not Loading

**Solution:**
```bash
python manage.py collectstatic --noinput
```

### Issue: Database Connection Error

**Solution:** Check DATABASE_URL environment variable is set correctly

### Issue: 502 Bad Gateway

**Solution:** 
- Check logs in your hosting platform
- Ensure gunicorn is installed
- Verify start command is correct

### Issue: File Uploads Not Persisting

**Solution:** 
- Free hosting has ephemeral storage
- Files uploaded may disappear after restart
- Consider using AWS S3 or Cloudinary for permanent storage

---

## 📱 Monitoring Your App

### Check Logs

**Render:**
- Go to your service → "Logs" tab

**PythonAnywhere:**
- Web tab → Error log / Server log

**Railway:**
- Click your service → "Deployments" → View logs

---

## 🔄 Updating Your Deployed App

### For Render/Railway (Auto-deploy):
```bash
git add .
git commit -m "Your update message"
git push origin main
```
→ Automatically deploys!

### For PythonAnywhere (Manual):
```bash
cd ~/dance-calendar-web
git pull
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
# Then click "Reload" button in Web tab
```

---

## 🎉 Success!

Your Dance Calendar Web app is now live and accessible to anyone with the URL!

**Next Steps:**
- Share the URL with your dance school
- Set up custom domain (optional, some platforms offer this)
- Monitor usage and upgrade plan if needed
- Set up regular backups of your database

---

## 📞 Need Help?

- Render Docs: https://render.com/docs
- PythonAnywhere Help: https://help.pythonanywhere.com
- Railway Docs: https://docs.railway.app

Good luck! 🕺💃
