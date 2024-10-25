from flask import Blueprint, abort, make_response, request
from ..db import db
from app.models.planet import Planet

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    color = request_body["color"]
    personality = request_body["personality"]

    new_planet = Planet(name=name, color=color, personality=personality)
    db.session.add(new_planet)
    db.session.commit()
    response = new_planet.to_dict()
    return response, 201
@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)

    planets_response = [planet.to_dict() for planet in planets]
    return planets_response
#
def validate_planet(planet_id, planets):
    # Narrow the errors - data error, type error
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Cat id {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message": f"Cat {planet_id} not found"}, 404))