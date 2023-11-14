from flask import Flask
from routes import app as poke_app

app = Flask(__name__)

app.register_blueprint(poke_app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)