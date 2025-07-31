from .models import Message
from .messages_repository import MessageRepository
from datetime import datetime

class MessageService:
    @staticmethod
    def process_and_store(data):
        required_fields = ['message_id', 'session_id', 'content', 'timestamp', 'sender']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Campo requerido faltante: {field}")

        try:
            timestamp = datetime.fromisoformat(data['timestamp'].replace('Z', '+00:00'))
        except Exception:
            raise ValueError("Formato de fecha inválido")

        message = Message(
            message_id=data['message_id'],
            session_id=data['session_id'],
            content=data['content'],  # Ya viene limpio desde el controlador
            timestamp=timestamp,
            sender=data['sender'],
            word_count=data['word_count'],  # Calculado previamente
            content_length=data['content_length']
        )
        return MessageRepository.save(message)

    @staticmethod
    def get_messages(session_id, sender=None, limit=20, offset=0):
        return MessageRepository.get_by_session_id(session_id, sender, limit, offset)