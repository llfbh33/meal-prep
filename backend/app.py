from flask import Flask
from flask_migrate import Migrate
from config import SQLALCHEMY_DATABASE_URI
from database import db
from models.user import User
from routes.user_routes import user_bp

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(user_bp, url_prefix='/users')

# Set up the database URL from environment variables
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

# Disable track modifications for Flask-SQLAlchemy (to avoid warnings)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database object and migration tool for postgres
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)


@app.route('/')
def home():
    return "Oh thank goodness!"

if __name__ == '__main__':
    app.run(debug=True)
