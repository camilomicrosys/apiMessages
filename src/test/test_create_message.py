import requests
import random
import string
from datetime import datetime

# URL base de tu API
BASE_URL = "http://localhost:5000"

# Endpoints
LOGIN_ENDPOINT = f"{BASE_URL}/auth/login"
CREATE_MESSAGE_ENDPOINT = f"{BASE_URL}/api/messages"

# Función para generar un message_id aleatorio
def generate_random_message_id():
    return "msg-" + ''.join(random.choices(string.digits, k=6))

def test_create_message():
    # 1. Hacer login para obtener el token JWT
    login_payload = {
        "email": "camilo@pruebas.com",
        "password": "1234"
    }

    login_response = requests.post(LOGIN_ENDPOINT, json=login_payload)
    assert login_response.status_code == 200, f"Error en login: {login_response.status_code} - {login_response.text}"

    token = login_response.json()["access_token"]

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # 2. Payload del mensaje a crear
    message_payload = {
        "message_id": generate_random_message_id(),
        "session_id": "session-abcdef",
        "content": "Hola, ¿cómo puedo ayudarte hoy?",
        "timestamp": datetime.utcnow().isoformat() + "Z",  # Formato UTC
        "sender": "system"
    }

    # 3. Crear el mensaje
    response = requests.post(CREATE_MESSAGE_ENDPOINT, json=message_payload, headers=headers)
    assert response.status_code in (200, 201), f"Error al crear mensaje: {response.status_code} - {response.text}"

    response_data = response.json()
    print("Mensaje creado:", response_data)

    # 4. Validaciones de los datos devueltos
    created_message = response_data.get("data", {})
    assert created_message.get("message_id") == message_payload["message_id"]
    assert created_message.get("session_id") == message_payload["session_id"]
    assert created_message.get("content") == message_payload["content"]
    assert created_message.get("sender") == message_payload["sender"]

# Ejecutar test si se corre directamente
if __name__ == "__main__":
    test_create_message()
