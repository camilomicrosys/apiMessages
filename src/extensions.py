from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flasgger import Swagger

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()
swagger = Swagger()


swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Documentación de la API Messages",
        "description": "Api para gestion de mensajes",
        "version": "1.0"
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Ingrese el token JWT como: Bearer <token>"
        }
    },
    "security": [{"Bearer": []}]
}

swagger = Swagger(template=swagger_template)