import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
from app.models.planet import Planet
import os


load_dotenv()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app 

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()    


@pytest.fixture
def three_saved_planets(app):
    planet1 = Planet(name="some_planet", description="rocky, no signs of life", size=100)
    planet2 = Planet(name="Earth", description="with lifeforms, water and land", size=5000)
    planet3 = Planet(name="Pluto", description="still a planet", size=200)

    db.session.add_all([planet1, planet2, planet3])
    db.session.commit()