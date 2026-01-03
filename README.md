# Dance Calendar Web - Quick Start

## 🚀 Quick Deploy to Render.com (5 minutes!)

### Option 1: Automatic Deploy with render.yaml

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/dance-calendar-web.git
   git push -u origin main
   ```

2. **Deploy on Render:**
   - Go to https://dashboard.render.com
   - Click "New" → "Blueprint"
   - Connect your GitHub repo
   - Render will automatically read `render.yaml` and set everything up!

### Option 2: Manual Setup

Follow the detailed instructions in [DEPLOYMENT.md](DEPLOYMENT.md)

---

## 🏠 Local Development

### Setup:
```bash
cd DANCE_CALENDAR_WEB
pip install -r ../requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Access:
- Web: http://localhost:8000
- Admin: http://localhost:8000/admin

---

## 📁 Project Structure

```
Dance_Calendar_Web/
├── DANCE_CALENDAR_WEB/          # Django project
│   ├── main/                    # Main app (calendar, groups, dancers)
│   ├── schedule/                # Schedule creation app
│   └── DANCE_CALENDAR_WEB/      # Settings
├── requirements.txt             # Python dependencies
├── build.sh                     # Build script for deployment
├── render.yaml                  # Render.com configuration
├── Procfile                     # For Heroku/Railway
├── .env.example                 # Environment variables template
└── DEPLOYMENT.md                # Full deployment guide
```

---

## 🔑 Environment Variables

Copy `.env.example` to `.env` and configure:

```env
DEBUG=True                                    # False in production
SECRET_KEY=your-secret-key                   # Generate new for production
ALLOWED_HOSTS=localhost,127.0.0.1            # Add your domain in production
DATABASE_URL=                                 # PostgreSQL URL (auto-set by Render)
```

---

## 📚 Documentation

- [Full Deployment Guide](DEPLOYMENT.md) - Step-by-step hosting instructions
- [Django Docs](https://docs.djangoproject.com/)

---

## ✨ Features

- 📅 Manage dance calendar and schedule
- 👥 Track dancers and couples
- 🏫 Organize groups and trainers
- 📊 Upload Excel files with availability
- 🤖 Automatic schedule generation with smart pairing
- 📈 Optimized scheduling algorithm

---

## 🆘 Quick Help

**Can't connect to database?**
→ Make sure DATABASE_URL is set (Render sets this automatically)

**Static files not loading?**
→ Run: `python manage.py collectstatic`

**Need to reset database?**
→ Run: `python manage.py migrate`

For more help, see [DEPLOYMENT.md](DEPLOYMENT.md)
