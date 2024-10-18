from flask import Blueprint
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
                "description" : planet.description
            }
        )
    return result_planets

