from flask import Blueprint
from app.models.planet import planets

# created blueprint
planets_bp = Blueprint("planets_bp",__name__, url_prefix=("/planets"))

@planets_bp.get("")
def get_all_planets():
    results_list = []
    for planet in planets:
        results_list.append(dict(
            id=planet.id,
            name=planet.name,
            desc=planet.description,
            size=planet.size
        ))
    return results_list

@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return {"message": f"planet {planet_id} is an invalid ID"}, 400
    
    for planet in planets:
        if planet.id == planet_id:
            return dict(
                id=planet.id,
                name=planet.name,
                desc=planet.description,
                size=planet.size
            )
    else:
        return {"message": f"planet {planet_id} not found"}, 404