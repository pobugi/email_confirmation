import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app_settings = config.DevelopmentConfig
    app.config.from_object(app_settings)

    db.init_app(app)

    from src.api import user_api

    app.register_blueprint(user_api)

    app.engine = create_engine(app.config["DATABASE_URL"], pool_size=5, pool_recycle=6)

    return app
