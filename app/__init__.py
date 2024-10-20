# from distutils.command.build_py import build_py

from flask import Flask
from .routes.planet_routes import planets_bp

# from .models.planet import Planet
# from .routes.planet_routes import planets_bp

def create_app(test_config=None):
    app = Flask(__name__)
    app.register_blueprint(planets_bp)
    return app


def main():
    app = create_app()
    app.run()


if __name__ == "__main__":
  
    main()