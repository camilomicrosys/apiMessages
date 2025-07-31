import requests

BASE_URL = "http://127.0.0.1:5000"
LOGIN_ENDPOINT = f"{BASE_URL}/auth/login"
MESSAGES_ENDPOINT = f"{BASE_URL}/api/messages/session-abcdef"


def test_get_messages_by_session_id():
    login_payload = {
        "email": "camilo@pruebas.com",
        "password": "1234"
    }

    login_response = requests.post(LOGIN_ENDPOINT, json=login_payload)
    assert login_response.status_code == 200, "Error en login"

    token = login_response.json()["access_token"]

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(MESSAGES_ENDPOINT, headers=headers)
    assert response.status_code == 200, "Error al obtener mensajes"

    data = response.json()
    print(data) 

    # Validamos que sea una lista de mensajes
    assert isinstance(data, list), "La respuesta no es una lista"
    assert len(data) > 0, "La lista de mensajes está vacía"

    # Validamos que cada mensaje tenga 'session_id' y otros campos esperados
    for msg in data:
        assert "session_id" in msg
        assert msg["session_id"] == "session-abcdef"
        assert "content" in msg  # Cambiado de 'message' a 'content'

