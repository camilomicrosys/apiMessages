from flask import Flask
from config import Config
from extensions import db, ma, jwt,swagger

from usersjwt.usersjwt_controller import usersjwt_controller
from loginjwt.loginjwt_controller import loginjwt_controller
from messages.message_controller import message_controller

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)
jwt.init_app(app)
swagger.init_app(app)


app.register_blueprint(usersjwt_controller)
app.register_blueprint(loginjwt_controller)
app.register_blueprint(message_controller)

@app.route('/')
def index():
    return 'API funcionando!'

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
