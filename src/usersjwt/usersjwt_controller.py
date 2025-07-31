from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from .usersjwt_service import UserService
from flasgger.utils import swag_from
from apidocs.login_docs import create_user_doc

usersjwt_controller = Blueprint('usersjwt_controller', __name__, url_prefix='/usersjwt')

@usersjwt_controller.route('/', methods=['POST'])
@swag_from(create_user_doc)
def create_user():
    return UserService.create_user(request.get_json())


@usersjwt_controller.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_user(id):
    return UserService.get_user_by_id(id)

