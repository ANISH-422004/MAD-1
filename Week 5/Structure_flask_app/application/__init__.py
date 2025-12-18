from flask import Flask
from .db import db
from .config import Config  # ✅ import config


def create_app():
    app = Flask(__name__)

    # ✅ Load config from class
    app.config.from_object(Config)

    # ✅ Initialize DB
    db.init_app(app)

    # ✅ Import models so SQLAlchemy sees them
    from . import models

    # ✅ Create tables
    with app.app_context():
        db.create_all()

    # ✅ Register blueprints
    from .controllers import post_bp

    app.register_blueprint(post_bp)

    return app
