
from flask import Blueprint
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



