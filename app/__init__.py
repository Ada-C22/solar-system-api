from flask import Flask
from .routes.planet_routes import planets_bp
from .db import db, migrate
from .models import planets
import os
from dotenv import load_dotenv


# Add configuration, such as registering blueprints or configuring databases
def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if config:
        app.config.update(config)
        
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(planets_bp)

    return app
