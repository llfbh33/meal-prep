import os
import sys
from flask import Flask
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import db
from models.user import User
from app import app

def seed_users():
    # Adding users to the list
    users = [
        User(username='Admin', email='aubriewoodbine@yahoo.com', password='password', hashed_password='password'),
        User(username='User2', email='silverBlueSpoon3@gmail.con', password='password', hashed_password='password'),
        User(username='User3', email='aubrie@valstorm.com', password='password', hashed_password='password'), 
    ]

    with app.app_context():  # Use app context for database operations
        for user in users:
            exists = User.query.filter_by(email=user.email).first()
            if not exists:
                db.session.add(user)
            
        db.session.commit()
        print('Users seeded successfully!')

if __name__ == "__main__":
    seed_users()
