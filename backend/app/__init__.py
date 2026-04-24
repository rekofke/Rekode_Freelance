from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # type: ignore

from .config import Config
from .models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    CORS(app)

    return app 