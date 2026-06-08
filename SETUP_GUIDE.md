# 🚀 Setup & Deployment Guide

## Quick Start (Local Development)

### Prerequisites
```bash
Node.js v18+
Python 3.11+
PostgreSQL 15+ atau Supabase account
Git
```

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Mac/Linux
# atau venv\Scripts\activate  # Windows
pip install -r requirements.txt
cp .env.example .env
# Edit .env dengan DATABASE_URL
python app.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## Database Setup

### Opsi 1: Supabase (Recommended)
1. Buat akun di https://supabase.com
2. Create new project
3. Di SQL Editor, jalankan:
   - database/schema.sql
   - database/initial_data.sql
4. Copy connection string ke .env (DATABASE_URL)

### Opsi 2: PostgreSQL Local
```bash
# Create database
psql -U postgres
CREATE DATABASE risiko_kppn;
CREATE USER risiko_user WITH PASSWORD 'risiko_secure_2024';
GRANT ALL PRIVILEGES ON DATABASE risiko_kppn TO risiko_user;

# Load schema
psql -U risiko_user -d risiko_kppn -f database/schema.sql
psql -U risiko_user -d risiko_kppn -f database/initial_data.sql
```

## Deployment

### Backend: Heroku
```bash
heroku create risiko-kppn
heroku config:set DATABASE_URL=your_supabase_url
git push heroku main
```

### Backend: AWS EC2
```bash
# SSH ke instance
ssh -i key.pem ubuntu@your-ip

# Setup
sudo apt update && sudo apt install -y python3-pip nginx
cd /var/www/
git clone repo
cd repo/backend
pip install -r requirements.txt

# Setup systemd service
sudo cat > /etc/systemd/system/risiko.service << EOF
[Unit]
Description=Risiko Backend
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/var/www/repo/backend
ExecStart=/usr/bin/python3 app.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable risiko
sudo systemctl start risiko
```

### Frontend: GitHub Pages
```bash
cd frontend
npm run build
npm run deploy
```

### Frontend: Vercel
```bash
npm install -g vercel
vercel
```

## User Setup

### Create Admin User
```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "email": "admin@kppn.local",
    "password": "AdminSecure2024!",
    "full_name": "Administrator",
    "role": "admin"
  }'
```

### Create Section Users
Ulangi untuk: MSKI, Bank, PD, Vera, Subbagian Umum

## Environment Variables

### Backend (.env)
```
DATABASE_URL=postgresql://user:pass@host/db
SECRET_KEY=your-secret
JWT_SECRET=your-jwt-secret
FLASK_ENV=production
PORT=5000
```

### Frontend (.env)
```
VITE_API_URL=http://backend-url/api
VITE_APP_NAME=Sistem Manajemen Risiko KPPN
```

## Troubleshooting

### Database Connection Error
- Verifikasi DATABASE_URL
- Cek firewall rules
- Test connection: `psql your_connection_string`

### CORS Error
- Backend harus punya CORS enabled
- Frontend API URL harus benar di .env

### Import Error (Python)
- Ensure venv activated
- Run: `pip install -r requirements.txt`

## Backup & Restore

### Backup Supabase
```bash
pg_dump "postgresql://user:pass@db.supabase.co:5432/db" > backup.sql
```

### Restore
```bash
psql "postgresql://user:pass@host/db" < backup.sql
```

## Support
Email: support@kppn.local  
Documentation: [docs/](./docs/)
