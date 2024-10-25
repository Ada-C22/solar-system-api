from flask import Flask
from .routes.planet_routes import planets_bp
from .db import db, migrate
from .models import planet

def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/planet'

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(planets_bp)

    return app


