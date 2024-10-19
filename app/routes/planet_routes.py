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
                "description" : planet.description,
                "distance_from_sun" : planet.distance_from_sun
            }
        )
    return result_planets

@planets_bp.get("/<id>")
def get_one_planet(id):
    for planet in planets:
        if planet.id == int(id):
            return {
            "id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "distance_from_sun" : planet.distance_from_sun
            }
    return {
        "error" : f"The planet with id:{id} was not found"
    }, 404
    
    
    

