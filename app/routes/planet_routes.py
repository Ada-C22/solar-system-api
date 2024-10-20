
from flask import Blueprint, abort, make_response
from app.models import planets
# from ..models.planet import Planet

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get("", strict_slashes=False)

def get_all_planet():
    result_list = []

    for planet in planets:
        result_list.append(
        {
            "id":planet.id,
            "name":planet.name,
            "description":planet.description,
            "moon":planet.moon

        }
        )
    return result_list


@planets_bp.get("/<planet_id>")

def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    # planet_id = int(planet_id)

    for planet in planets:
        if planet_id == planet_id:
            return[{
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "moon": planet.moon
            }]
    return {"message": f"planet {planet_id} not found"}, 404

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response = {"messsage": f"Planet {planet_id} invalid"}
        abort(make_response(response,400))
    
    for planet in planets:
        if planet.id == planet_id:
            return planet
    
    response = {"message": f"planet {planet_id} not found"}
    abort(make_response(response, 404))