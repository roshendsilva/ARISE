import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'arise-catholic-apologetics-secret-key-2026-god-is-truth')
    
    # Default live Supabase PostgreSQL database connection URL
    DEFAULT_SUPABASE_URI = 'postgresql://postgres.kbulscucdcexqnudfgec:Roshen%402026@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres'
    
    raw_url = os.environ.get('DATABASE_URL') or ''
    db_url = raw_url.strip().replace('\r', '').replace('\n', '') or DEFAULT_SUPABASE_URI
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)

    # Auto-encode un-encoded '@' in password if present
    if "sqlite" not in db_url and db_url.count("@") > 1:
        try:
            scheme_end = db_url.find("://") + 3
            last_at_idx = db_url.rfind("@")
            user_pass = db_url[scheme_end:last_at_idx]
            host_part = db_url[last_at_idx + 1:]
            
            if ":" in user_pass:
                user, password = user_pass.split(":", 1)
                password = password.replace("@", "%40")
                db_url = f"postgresql://{user}:{password}@{host_part}"
        except Exception:
            pass
        
    # Ensure sslmode=require for Supabase cloud PostgreSQL connections on Vercel
    if "sqlite" not in db_url and "sslmode" not in db_url:
        if "?" in db_url:
            db_url += "&sslmode=require"
        else:
            db_url += "?sslmode=require"

    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = int(os.environ.get('PORT', 5001))
