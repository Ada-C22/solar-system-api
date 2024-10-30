from flask import Blueprint, abort, make_response, request, Response
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
    query = db.select(Planet)

    namesake_param = request.args.get("namesake")
    if namesake_param:
        query = query.where(Planet.namesake.ilike(f"%{namesake_param}%"))

    distance_from_sun_param = request.args.get("distance_from_sun")
    if distance_from_sun_param:
        query = query.where(Planet.distance_from_sun <= distance_from_sun_param).order_by("surface_area")

    query = query.order_by(Planet.id)

    planets = db.session.scalars(query)

    planets_response = [planet.to_dict() for planet in planets]
    return planets_response

@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    planet_response = planet.to_dict()
    return planet_response

@planets_bp.put("/<planet_id>")
def update_one_planet(planet_id):
    planet = validate_planet(planet_id)
    response_body = request.get_json()

    planet.name = response_body["name"]
    planet.surface_area = response_body["surface_area"]
    planet.moons = response_body["moons"]
    planet.distance_from_sun = response_body["distance_from_sun"]
    planet.namesake = response_body["namesake"]

    db.session.commit()

    return Response(status=204, mimetype="application/json")

@planets_bp.delete("/<planet_id>")
def delete_one_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

#Helper functions
def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        abort(make_response({"message": f"Planet with {planet_id} is invalid"}, 400))

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)
    
    if not planet:
        abort(make_response({"message": f"Planet with {planet_id} is not found"}, 404))
    
    return planet