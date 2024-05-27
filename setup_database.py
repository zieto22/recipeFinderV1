# setup_database.py
from app import app, db
from models import User, Todo

with app.app_context():
    """
    This script sets up the database and creates the necessary tables.
    """

    db.create_all()
    print("Database and tables created.")
