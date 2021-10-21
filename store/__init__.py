"""
Application Factory
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from config import Config



db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()


def create_app(config_name):
    app = Flask(__name__)

    # app configurations
    app.config.from_object(Config)
    Config.init_app(app)

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # register blueprints
    from .main import main
    app.register_blueprint(main)

    return app