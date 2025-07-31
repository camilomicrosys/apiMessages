create_user_doc = {
    'tags': ['Usuarios JWT'],
    'description': 'Crea un nuevo usuario con email y contraseña, para posteriormente loguearlo con el api de login',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {'type': 'string', 'example': 'camilo@pruebas.com'},
                    'password': {'type': 'string', 'example': '1234'}
                },
                'required': ['email', 'password']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Usuario creado exitosamente.'
        },
        400: {
            'description': 'Datos inválidos o usuario ya existente.'
        }
    }
}

login_user_doc = {
    'tags': ['Autenticación'],
    'description': 'Inicia sesión con email y contraseña, para obtener el token que requerira las demas api',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {'type': 'string', 'example': 'camilo@pruebas.com'},
                    'password': {'type': 'string', 'example': '1234'}
                },
                'required': ['email', 'password']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Inicio de sesión exitoso, devuelve token JWT.'
        },
        401: {
            'description': 'Credenciales incorrectas.'
        }
    }
}
