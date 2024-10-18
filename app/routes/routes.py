from flask import Blueprint
from ..models.planet import planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get("")
def get_all_planets():
    results_list = []
    for planet in planets:
        results_list.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            distance_from_earth=planet.distance_from_earth
        ))
    return results_list

