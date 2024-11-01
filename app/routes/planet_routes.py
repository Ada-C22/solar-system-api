from flask import Blueprint, abort, make_response, request, Response
from app.models.planet import Planet
from ..db import db

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    num_moons = request_body["num_moons"]
    
    new_planet = Planet(name=name, description=description, num_moons=num_moons)
    db.session.add(new_planet)
    db.session.commit()

    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "num_moons": new_planet.num_moons
    }
    return response, 201 


@planets_bp.get("")
def get_all_planets():

    query = db.select(Planet)

    description_param = request.args.get("description")

    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))

    num_moons_param = request.args.get("num_moons")

    if num_moons_param:
        query = query.where(Planet.num_moons == num_moons_param)

    query = query.order_by(Planet.id)
    planets = db.session.scalars(query)
    
    planets_response = [] 
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "num_moons": planet.num_moons 
                }
        )
    return planets_response

@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "num_moons": planet.num_moons, 
    }

@planets_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.num_moons = request_body["num_moons"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@planets_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

def validate_planet(planet_id):
    try:
        planet_id =int(planet_id)
    except:
        response = {"message": f"Planet {planet_id} invalid."} 
        abort(make_response(response, 400))

    query = db.select(Planet).where(Planet.id==planet_id)
    planet = db.session.scalar(query)

    if not planet:
        response = {"message": f"Planet {planet_id} not found."}
        abort(make_response(response, 404))

    return planet



# @planets_bp.get("")
# def get_all_planets():
#     results_list = []

#     for planet in planets:
#         results_list.append(dict(
#             id=planet.id, 
#             name=planet.name,
#             description=planet.description,
#             num_moon=planet.num_moons
#         ))

#     return results_list

# @planets_bp.get("/<planet_id>")
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)
#     return planet.to_dict(), 200


# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message": f"Planet {planet_id} is invalid."}, 400))
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
#     abort(make_response({"message": f"Planet {planet_id} is not found."}, 404))    