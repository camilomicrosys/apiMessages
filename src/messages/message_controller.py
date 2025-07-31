from flask import Blueprint, request, Response, jsonify
from collections import OrderedDict
import json
from .message_service import MessageService
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from flask_jwt_extended import jwt_required

from flasgger import swag_from
from apidocs.messages_docs import create_message_doc, get_message_by_id_doc

from .filters import validate_message_payload, MessageValidationError


message_controller = Blueprint('messages', __name__, url_prefix='/api/messages')

@message_controller.route('', methods=['POST'])
@jwt_required()
@swag_from(create_message_doc)
def create_message():
    try:
        data = request.get_json()

        #  Validar y procesar el contenido
        validated_data = validate_message_payload(data)

        # Guardar el mensaje procesado
        message = MessageService.process_and_store(validated_data)

        # Armar respuesta con los datos procesados desde validated_data
        response_data = OrderedDict([
            ("status", "success"),
            ("data", OrderedDict([
                ("message_id", message.message_id),
                ("session_id", message.session_id),
                ("content", message.content),
                ("timestamp", message.timestamp.isoformat() + "Z"),
                ("sender", message.sender),
                ("metadata", OrderedDict([
                    ("word_count", validated_data["word_count"]),
                    ("character_count", validated_data["content_length"]),
                    ("processed_at", datetime.utcnow().isoformat() + "Z")
                ]))
            ]))
        ])

        return Response(
            json.dumps(response_data, indent=4),
            mimetype='application/json',
            status=201
        )

    except MessageValidationError as ve:
        return Response(
            json.dumps({
                "status": "error",
                "code": ve.code,
                "message": ve.message,
                "details": ve.details
            }),
            mimetype='application/json',
            status=400
        )

    except IntegrityError as ie:
        if "Duplicate entry" in str(ie.orig):
            return Response(
                json.dumps({"status": "error", "message": "Ya existe un mensaje con ese message_id"}),
                mimetype='application/json',
                status=409
            )
        return Response(
            json.dumps({"status": "error", "message": "Error de integridad en la base de datos"}),
            mimetype='application/json',
            status=500
        )

    except Exception:
        return Response(
            json.dumps({"status": "error", "message": "Error interno del servidor"}),
            mimetype='application/json',
            status=500
        )







@message_controller.route('/<session_id>', methods=['GET'])
@jwt_required()
@swag_from(get_message_by_id_doc)
def get_messages(session_id):
    sender = request.args.get('sender')
    try:
        limit = int(request.args.get('limit', 20))
        offset = int(request.args.get('offset', 0))
    except ValueError:
        return jsonify({"error": "Parámetros de paginación inválidos"}), 400

    messages = MessageService.get_messages(session_id, sender, limit, offset)
    return jsonify([{
        "message_id": m.message_id,
        "session_id": m.session_id,
        "content": m.content,
        "timestamp": m.timestamp.isoformat(),
        "sender": m.sender,
        "word_count": m.word_count,
        "content_length": m.content_length
    } for m in messages]), 200
