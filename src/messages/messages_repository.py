from .models import Message
from extensions import db

class MessageRepository:
    @staticmethod
    def save(message):
        db.session.add(message)
        db.session.commit()
        return message

    @staticmethod
    def get_by_session_id(session_id, sender=None, limit=20, offset=0):
        query = Message.query.filter_by(session_id=session_id)
        if sender:
            query = query.filter_by(sender=sender)
        return query.order_by(Message.timestamp).limit(limit).offset(offset).all()