from datetime import datetime

class MessageValidationError(Exception):
    def __init__(self, field, detail):
        self.code = "INVALID_FORMAT"
        self.message = "Formato de mensaje inválido"
        self.details = detail
        super().__init__(f"{field}: {detail}")

# Lista de palabras inapropiadas a censurar
BAD_WORDS = ["grosería1", "grosería2", "grosería3"]

def sanitize_content(content):
    """
    Reemplaza las palabras inapropiadas por '***' (ignorando mayúsculas)
    """
    for word in BAD_WORDS:
        content = content.replace(word, "***")
        content = content.replace(word.capitalize(), "***")
        content = content.replace(word.upper(), "***")
    return content

def validate_message_payload(data):
    required_fields = ["message_id", "session_id", "content", "timestamp", "sender"]

    for field in required_fields:
        if field not in data:
            raise MessageValidationError(field, f"El campo '{field}' es obligatorio")

    if not isinstance(data["message_id"], str):
        raise MessageValidationError("message_id", "Debe ser una cadena")

    if not isinstance(data["session_id"], str):
        raise MessageValidationError("session_id", "Debe ser una cadena")

    if not isinstance(data["content"], str):
        raise MessageValidationError("content", "Debe ser una cadena")

    try:
        # Solo validar formato ISO, no convertir
        datetime.fromisoformat(data["timestamp"].replace("Z", ""))
    except ValueError:
        raise MessageValidationError("timestamp", "Debe tener formato ISO válido")

    if data["sender"] not in ["user", "system"]:
        raise MessageValidationError("sender", "El campo 'sender' debe ser 'user' o 'system'")

    # Procesamiento adicional del contenido
    original_content = data["content"]
    sanitized_content = sanitize_content(original_content)

    word_count = len(sanitized_content.split())
    content_length = len(sanitized_content)

    # Mutamos los datos directamente
    data["content"] = sanitized_content
    data["word_count"] = word_count
    data["content_length"] = content_length

    return data
