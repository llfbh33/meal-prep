from flask import Blueprint, request, jsonify
from database import db
from models.user import User

user_bp = Blueprint("user", __name__)

@user_bp.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])

@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.json
    new_user = User(name=data["name"], email=data["email"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created!"}), 201
