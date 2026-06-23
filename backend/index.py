# backend/index.py

from app import create_app

# Vercel akan mencari variabel bernama 'app' di dalam file ini
app = create_app()