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
    "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI'),
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
  # Arrange
  earth = Planet(name="Earth",
                 description='Earth is the fifth largest planet in our solar system and is the largest of the terrestrial planets',
                 diameter=7926)
  jupiter = Planet(name='Jupiter',
                   description='Jupiter is the fifth planet from the Sun and the largest in the Solar System',
                   diameter=86881)
  
  db.session.add_all([earth, jupiter])
  db.session.commit()
