from extensions import db

class Message(db.Model):
    __tablename__ = 'messages'

    message_id = db.Column(db.String(36), primary_key=True)  # UUID por ejemplo
    session_id = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    sender = db.Column(db.String(20), nullable=False)  # "user" o "system"
    word_count = db.Column(db.Integer)
    content_length = db.Column(db.Integer)