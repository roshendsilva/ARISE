import sys
import os

# Add parent directory to path so Flask app can import models, config, seed_data
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
