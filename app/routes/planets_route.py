from flask import Blueprint, abort, make_response
from app.models.planets import planet_list

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get("")
def get_all_planets():
    results_list = []

    for planet in planet_list:
        results_list.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            size=planet.size
        ))

    return results_list

@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            size=planet.size
        )

def validate_planet(id):
    try: 
        id = int(id)
    except ValueError:
        abort(make_response({"message": f"Planet id {id} invalid"}, 400))

    for planet in planet_list:
        if planet.id == id:
            return planet
    abort(make_response({"message": f"Planet id {id} not found"}, 404))



