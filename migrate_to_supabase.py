import sys
import os
sys.path.append(r"c:\Users\joyce evangeline\OneDrive\Desktop\Apologetics")

from app import app, db
from seed_data import seed_database

def migrate():
    print("=" * 60)
    print("ARISE Platform — Supabase PostgreSQL Migration Tool")
    print("=" * 60)
    print(f"Current Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

    if "sqlite" in app.config['SQLALCHEMY_DATABASE_URI']:
        print("\n[NOTICE] Currently using local SQLite.")
        print("To connect to Supabase:")
        print("1. Open your .env file")
        print("2. Replace DATABASE_URL with your Supabase Connection String:")
        print("   DATABASE_URL=postgresql://postgres.[ref]:[password]@aws-0-[region].pooler.supabase.com:6543/postgres")
        print("3. Run this script again: python migrate_to_supabase.py\n")
        return

    print("\nConnecting to Supabase PostgreSQL...")
    with app.app_context():
        try:
            db.create_all()
            print("Successfully created PostgreSQL tables on Supabase!")
            seed_database(app)
            print("Successfully seeded all 88 articles, Patristic timeline, and categories to Supabase PostgreSQL!")
        except Exception as e:
            print(f"[ERROR] Migration failed: {e}")

if __name__ == '__main__':
    migrate()
