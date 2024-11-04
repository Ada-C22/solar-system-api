from flask import Blueprint, abort, make_response, request, Response
from ..models.planet import Planet
from ..db import db
from sqlalchemy import asc, desc
from .routes_utilities import validate_model

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    
    try:
        new_planet = Planet.from_dict(request_body)
    except KeyError as e:
        response = {
            "message": f"Invalid request: missing {e.args[0]}"
        }
        abort(make_response(response, 400))
    db.session.add(new_planet)
    db.session.commit()

    response = new_planet.to_dict()
    return response, 201

@planets_bp.get("")
def get_all_planets():
    sort_param = request.args.get("sort")
    order_param = request.args.get("order", "asc") # Default to ascending if not specified

    query = db.select(Planet)

    if sort_param:
        sort_column = getattr(Planet, sort_param, None)
        if sort_column:
            query = query.order_by(asc(sort_column) if order_param == "asc" else desc(sort_column))

    namesake_param = request.args.get("namesake")
    if namesake_param:
        query = query.where(Planet.namesake.ilike(f"%{namesake_param}%"))

    distance_from_sun_param = request.args.get("distance_from_sun")
    if distance_from_sun_param:
        query = query.where(Planet.distance_from_sun <= distance_from_sun_param)
    query = query.order_by(Planet.id)

    planets = db.session.scalars(query)

    planets_response = [planet.to_dict() for planet in planets]
    return planets_response
    
@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    planet_response = planet.to_dict()
    return planet_response

@planets_bp.put("/<planet_id>")
def update_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
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
    planet = validate_model(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")
