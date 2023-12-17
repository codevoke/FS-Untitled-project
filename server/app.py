import os

from flask import Flask
from dotenv import load_dotenv

from models import db
from resources import api

load_dotenv()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('PRODUCTION_DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

db.init_app(app)
api.init_app(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0')