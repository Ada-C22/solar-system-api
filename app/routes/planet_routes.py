from flask import Blueprint, abort, make_response
from app.models import planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get("", strict_slashes=False)
def get_all_planet():
    result_list = []
    for planet in planets:
        result_list.append(planet.__dict__)
    return result_list


@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    if not planet_id.isnumeric():
        response = {"message": f"Planet {planet_id} invalid"}
        abort(make_response(response, 400))

    for planet in planets:
        if planet.id == int(planet_id):
            return planet.__dict__

    response = {"message": f"planet {planet_id} not found"}
    abort(make_response(response, 404))