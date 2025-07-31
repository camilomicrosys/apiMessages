from flask import Flask
from config import Config
from extensions import db, ma, jwt,swagger



app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)
jwt.init_app(app)
swagger.init_app(app)



@app.route('/')
def index():
    return 'API funcionando!'

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
