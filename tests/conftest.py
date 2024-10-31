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
def get_every_single_planet(app):
    planet = [Planet(name="Coruscant",
                      description="City-covered planet that served as the seat of government for the Galactic Republic and Empire",
                      moon=4),
               Planet(name="Tatooine",
                      description="Desert world with binary suns, home to the Skywalker family and Jabba the Hutt",
                      moon=3), Planet(name="Naboo",
                      description="Beautiful planet with rolling plains and vast seas, homeworld of Padmé Amidala",
                      moon=1),
               Planet(name="Hoth", description="Frozen ice planet that briefly served as a Rebel Alliance base",
                      moon=2),

               Planet(name="Endor",
               description="Forest moon home to the Ewoks and site of the second Death Star's destruction",
               moon=9)]
    db.session.add_all(planet)
    db.session.commit()

@pytest.fixture
def get_planet_invalid_id(app):
    return "abc"

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
    
@pytest.fixture
def update_existing_planet(app):
    kronos= Planet(name ="Kronos", description = "Homeword of the Klingon Empire, rich in warrior culture and tradition, featuring magnificent cities built among dramatic mountain ranges, home to the legendary Great Hall of the High Council, and birthplace of many of the quadrant's greatest warriors and most honored traditions", moon = 7)
    db.session.add(kronos)
    db.session.commit()

@pytest.fixture
def delete_existing_planet_romulus(app):
    romulus =  Planet(name = "Romulus", description = "Homeworld of the Romulan Star Empire, featuring green-tinted skies and advanced architecture.", moon = 2)
    db.session.add(romulus)
    db.session.commit()
    