from .usersjwt_repository import UserRepository
from .schemas import user_schema, users_schema
from flask import jsonify

class UserService:
    @staticmethod
    def create_user(data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"message": "Email y contraseña son requeridos"}), 400

        if UserRepository.find_by_email(email):
            return jsonify({"message": "Email ya registrado"}), 400

        user = UserRepository.create_user(email, password)
        return user_schema.jsonify(user), 201


    @staticmethod
    def get_user_by_id(id):
        user = UserRepository.get_by_id(id)
        if not user:
            return jsonify({"message": "Usuario no encontrado"}), 404
        return user_schema.jsonify(user), 200
