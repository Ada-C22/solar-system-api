from flask import Blueprint, abort, make_response, request, Response
from ..db import db
from app.models.planets import Planet

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    size = request_body["size"]

    new_planet = Planet(name=name, description=description, size=size)
    db.session.add(new_planet)
    db.session.commit()

    response = new_planet.to_dict()
    return response, 201

@planets_bp.get("")
def get_all_planets():
    # query = db.select(Planet).order_by(Planet.id)
    # planets = db.session.scalars(query)

    # planets_response = [planet.to_dict() for planet in planets]
    # return planets_response
        query = db.select(Planet)
        name_param = request.args.get("name")

        if name_param:
        # restrict to matching planet
            query = query.where(Planet.name == name_param)
    
        description_param = request.args.get("description")
        
        if description_param:
        # restrict to matching planet
            query = query.where(Planet.description.ilike(f"%{description_param}%"))
    
        size_param = request.args.get("size")
        if size_param:
        # restrict to matching planet
            query = query.where(Planet.ilike(f"%{size_param}%"))
    
        query = query.order_by(Planet.id)
        planets = db.session.scalars(query)

        planets_response = [planet.to_dict() for planet in planets]
        return planets_response


@planets_bp.get("/<planet_id>")
def get_single_planet(planet_id):
    planet = validate_planet(planet_id)

    return planet.to_dict()

@planets_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.size = request_body["size"]

    db.session.commit()

    return Response(status=204, mimetype='application/json')

@planets_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype='application/json')

def validate_planet(planet_id):
    try: 
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"Planet id {planet_id} invalid"}, 400))

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    # for planet in Planet:
    #     if planet.id == id:
    #         return planet
    # abort(make_response({"message": f"Planet id {id} not found"}, 404))

    if not planet:
        abort(make_response({"message": f"Planet {planet_id} not found"}, 404))

    return planet



