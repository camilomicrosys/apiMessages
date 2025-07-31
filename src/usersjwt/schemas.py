from flask_marshmallow import Marshmallow
from .models import UserJWT

ma = Marshmallow()

class UserJWTSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserJWT
        load_instance = True
        exclude = ("password_hash",)  # No mostrar password hash en respuestas

user_schema = UserJWTSchema()
users_schema = UserJWTSchema(many=True)