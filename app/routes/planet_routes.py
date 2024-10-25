from flask import Blueprint, abort, make_response, request
from app.models.planet import Planet
from ..db import db

# created blueprint
planets_bp = Blueprint("planets_bp",__name__, url_prefix=("/planets"))

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description= request_body["description"]
    size = request_body["size"]

    new_planet = Planet(name=name, description=description, size=size)
    db.session.add(new_planet)
    db.session.commit()

    response = new_planet.to_dict()
    return response, 201

# @cats_bp.get("")
# def get_all_cats():
#     query = db.select(Cat).order_by(Cat.id)
#     cats = db.session.scalars(query)

#     cats_response = [cat.to_dict() for cat in cats]
#     return cats_response


# @planets_bp.get("")
# def get_all_planets():
#     results_list = []

#     for planet in planets: 
#         results_list.append(planet.to_dict())
#     return results_list
    

# @planets_bp.get("/<planet_id>")
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)
#     return planet.to_dict()
    
# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError:
#         abort(make_response({"message": f"planet {planet_id} is an invalid ID"}, 400))
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
#     else:
#         abort(make_response({"message": f"planet {planet_id} not found"}, 404))