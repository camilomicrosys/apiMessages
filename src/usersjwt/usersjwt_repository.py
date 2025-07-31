from .models import UserJWT
from extensions import db
from flask import jsonify

class UserRepository:
    @staticmethod
    def get_all():
        return UserJWT.query.all()

    @staticmethod
    def find_by_email(email):
        return UserJWT.query.filter_by(email=email).first()

    @staticmethod
    def get_by_id(user_id):
        return UserJWT.query.get(user_id)

    @staticmethod
    def create_user(email, password):
        user = UserJWT(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user
