from flask import Blueprint, abort, make_response, request, Response
from app.models.planets import Planet
from ..db import db
from sqlalchemy import func

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

#Function gives end user ability to search api by ID or by Name
def validate_planet_identifier(planet_identifier):
    # Checks if id is int or name. If id return id function if str return name function
    if planet_identifier.isdigit():
        return validate_planet_id(planet_identifier)
    else:
        return validate_planet_name(planet_identifier)

# checks if user requested valid planet id and returns 404 if user enters unknown planet id
def validate_planet_id(planet_id):
    try:
        planet_id = int(planet_id) 
    except:
        response = {"message": f"planet {planet_id} invalid"}
        abort(make_response(response, 400))

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    if not planet:
        abort(make_response({"message": f"planet {planet_id} not found"}, 404))
    
    return planet

# checks if user requested valid planet name and returns 404 if user enter unknown planet name
def validate_planet_name(planet_name):
    planet_name = planet_name.lower()
    query = db.select(Planet).where(func.lower(Planet.name) == planet_name)
    planet = db.session.scalar(query)

    if not planet:
        abort(make_response({"message": f"planet {planet_name} not found"}, 404))
    
    return planet

# Wave 4
@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    distance_from_sun = request_body["distance_from_sun"]


    new_planet = Planet(name=name, description=description, distance_from_sun=distance_from_sun)
    db.session.add(new_planet)
    db.session.commit()

    response = new_planet.get_dict()
    return response, 201

# Wave 2 and 3
@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet)
    
# Wave 5 - Created parameters to make filtering through Data easier
    name_param = request.args.get("name")
    if name_param:
        query = query.where(Planet.name.ilike(f"%{name_param}%"))

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))
    
    distance_from_sun_param = request.args.get("distance_from_sun")
    if distance_from_sun_param:
        query = query.where(Planet.description.ilike(f"%{distance_from_sun_param}%"))

    query = query.order_by(Planet.id)

    planets = db.session.scalars(query)

    planets_response = [planet.get_dict() for planet in planets]
    return planets_response

@planets_bp.get("/<planet_identifier>") # updated planet_id to planet_identifier to make more descriptive for both name and id
def get_one_planet(planet_identifier):
    planet = validate_planet_identifier(planet_identifier)
    return planet.get_dict()

#Wave 4 
@planets_bp.put("<planet_identifier>")
def update_planet(planet_identifier):
    planet = validate_planet_identifier(planet_identifier)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.distance_from_sun = request_body["distance_from_sun"]
    db.session.commit()

    return Response(status=204, mimetype='application/json')

@planets_bp.delete("<planet_identifier>")
def delete_planet(planet_identifier):
    planet = validate_planet_identifier(planet_identifier)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype='application/json')
