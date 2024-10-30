import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
import os
from app.models.planet import Planet

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
def two_saved_planets(app):
    mercury = Planet(name = "Mecury", description = "the hotess next to the sun", moon = 0)
    vulcan = Planet(name = "Vulcan", description = "the best", moon = 2)
    db.session.add_all([mercury, vulcan])
    db.session.commit()

@pytest.fixture
def create_new_planet(app):
    romulus =  Planet(name = "Romulus", description = "Homeworld of the Romulan Star Empire, featuring green-tinted skies and advanced architecture.", moon = 2)
    db.session.add(romulus)
    db.session.commit()