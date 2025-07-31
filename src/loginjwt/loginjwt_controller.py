from flask import Blueprint, request, jsonify
from .loginjwt_service import AuthService
from flasgger.utils import swag_from
from apidocs.login_docs import login_user_doc

loginjwt_controller = Blueprint('loginjwt_controller', __name__, url_prefix='/auth')

@loginjwt_controller.route('/login', methods=['POST'])
@swag_from(login_user_doc)
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    return AuthService.login_user(email, password)
