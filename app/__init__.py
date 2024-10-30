from importlib import import_module

from flask import Flask
from .routes.planet_routes import planets_bp
from .db import db, migrate
from .models import planet
import os

def create_app(config=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    # the base conf
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/planet'

    if config:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
        app.config.update(config)
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')


    db.init_app(app)
    migrate.init_app(app, db)


    app.register_blueprint(planets_bp)

    return app

