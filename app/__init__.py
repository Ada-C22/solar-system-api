from flask import Flask
from .routes.planet_routes import planets_bp


def create_app(test_config=None):
    app = Flask(__name__)
    # registered the planets blueprint with the app
    app.register_blueprint(planets_bp)

    return app
