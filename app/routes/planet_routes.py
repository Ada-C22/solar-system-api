from flask import Blueprint, abort, make_response, request
from app.models.planet import Planet
from ..db import db

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.get("")
def get_all_planets():
  query = db.select(Planet).order_by(Planet.id)
  planets = db.session.scalars(query)

  planet_response = []
  for planet in planets:
    planet_response.append(
        {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "diameter": planet.diameter,
        }
    )
  return planet_response

@planet_bp.post("")
def create_planet():
  request_body = request.get_json()
  name = request_body["name"]
  description = request_body["description"]
  diameter = request_body["diameter"]

  new_planet = Planet(name=name, description=description, diameter=diameter)
  db.session.add(new_planet)
  db.session.commit()

  response = {
    "id": new_planet.id,
    "name": new_planet.name,
    "description": new_planet.description,
    "diameter": new_planet.diameter,
  }

  return response, 201



