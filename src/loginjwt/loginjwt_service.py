from usersjwt.usersjwt_repository import UserRepository
from flask_jwt_extended import create_access_token
from flask import jsonify

class AuthService:
    @staticmethod
    def login_user(email, password):
        user = UserRepository.find_by_email(email)

        if not user or not user.check_password(password):
            return jsonify({"error": "Invalid credentials"}), 401

        token = create_access_token(identity=user.email)
        return jsonify({"access_token": token}), 200
