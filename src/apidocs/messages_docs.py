create_message_doc = {
    "tags": ["Mensajes"],
    "description": "Esta api permite la creacion de un nuevo mensaje, Authorization: Bearer Token, debes consumir la api de login para obtener este token",
    "security": [{"Bearer": []}],  # <-- Esta línea es clave
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "message_id": {"type": "string"},
                    "session_id": {"type": "string"},
                    "content": {"type": "string"},
                    "timestamp": {"type": "string"},
                    "sender": {"type": "string"},
                },
                "required": ["message_id", "session_id", "content", "sender"]
            }
        }
    ],
    "responses": {
        "201": {"description": "Mensaje creado"},
        "400": {"description": "Datos inválidos"},
        "401": {"description": "No autorizado"}
    }
}

get_message_by_id_doc = {
    "tags": ["Mensajes"],
    "description": "Esta api permite la obtencion de mensajes por sesion_id de conversacion , permite paginacion ofset, u obtener mensajes por sender, Authorization: Bearer Token, debes consumir la api de login para obtener este token",
    "security": [{"Bearer": []}],  # <-- Aquí también
    "parameters": [
        {
            "name": "session_id",
            "in": "path",
            "type": "string",
            "required": True
        },
        {
            "name": "sender",
            "in": "query",
            "type": "string",
            "required": False
        },
        {
            "name": "limit",
            "in": "query",
            "type": "integer",
            "required": False,
            "default": 20
        },
        {
            "name": "offset",
            "in": "query",
            "type": "integer",
            "required": False,
            "default": 0
        }
    ],
    "responses": {
        "200": {"description": "Mensajes encontrados"},
        "401": {"description": "No autorizado"},
        "404": {"description": "No encontrado"}
    }
}
