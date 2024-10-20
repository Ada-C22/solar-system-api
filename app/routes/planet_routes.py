from flask import Blueprint, abort, make_response
from app.models.planet import planets


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get("")
def get_all_planets():
    result_planets = []
    for planet in planets:
        result_planets.append(
            {
                "id" : planet.id,
                "name": planet.name,
                "description" : planet.description,
                "distance_from_sun" : planet.distance_from_sun
            }
        )
    return result_planets

# Helper function for error handling
def validate_planet(id):
    try:
        input_id = int(id)
    except:
        response = make_response(f"Planet id: {id} not found. Enter a valid planet number from 1 to 8.", 404)
        abort(response)
    
    for planet in planets:
        if planet.id == input_id:
            return planet
    response = make_response(f"Planet id: {id} not found. Enter planet id from 1 to 8, 404")
    abort(response)
    

@planets_bp.get("/<id>")
def get_one_planet(id):
    
    planet = validate_planet(id)
    return {
    "id" : planet.id,
    "name" : planet.name,
    "description" : planet.description,
    "distance_from_sun" : planet.distance_from_sun
    }
    
    
    
    

