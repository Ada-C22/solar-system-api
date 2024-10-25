from flask import Blueprint, abort, make_response, request
from ..models.planet import Planet
from ..db import db

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    surface_area = request_body["surface_area"]
    moons = request_body["moons"]
    distance_from_sun = request_body["distance_from_sun"]
    namesake = request_body["namesake"]

    new_planet = Planet(name=name, surface_area=surface_area, moons=moons, distance_from_sun=distance_from_sun, namesake=namesake)
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

# @planets_bp.get("")
# def get_all_planets():
#     results_list = []
#     for planet in planets:
#         results_list.append(planet.to_dict())
#     return results_list

# @planets_bp.get("/<planet_id>")
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)
#     return planet.to_dict(), 200


#Helper functions
def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        abort(make_response({"message": f"Planet with {planet_id} is invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet
    
    abort(make_response({"message": f"Planet with {planet_id} is not found"}, 404))