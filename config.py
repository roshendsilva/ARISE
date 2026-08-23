import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'arise-catholic-apologetics-default-secret-key')
    
    # Handle database URL for SQLite or Supabase/Postgres
    db_url = os.environ.get('DATABASE_URL', 'sqlite:///arise.db')
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)
        
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = int(os.environ.get('PORT', 5001))
