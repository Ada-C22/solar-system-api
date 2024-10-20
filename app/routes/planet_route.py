from flask import Blueprint
from app.models.planets import planets
from flask import Blueprint, abort, make_response

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get("")
def get_all_planets():
    planets_list = []
    for planet in planets:
        planets_list.append(
            {
                "id":planet.id,
                "name":planet.name,
                "description":planet.description  
            }
        )
    return planets_list


@planets_bp.get("/<planet_identifier>") # updated planet_id to planet_identifier to make more descriptive for both name and id
def get_one_planet(planet_identifier):
    planet = validate_planet_identifier(planet_identifier)

    return {
        "id": planet.id,
        "title": planet.name,
        "description": planet.description,
        "distance_from_sun": planet.distance_from_sun
    }


def validate_planet_identifier(planet_identifier):
    # check if id is int or name. If id return id function if str return name function
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

    for planet in planets:
        if planet.id == planet_id:
            return planet

    response = {"message": f"planet {planet_id} not found"}
    abort(make_response(response, 404))

# checks if user requested valid planet name and returns 404 if user enter unknown planet name
def validate_planet_name(planet_name):
    for planet in planets:
        if planet.name.lower() == planet_name.lower():
            return planet
    
    response = {"message": f"planet {planet_name} not found"}
    abort(make_response(response), 404)