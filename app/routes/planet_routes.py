from flask import Blueprint, abort, make_response, request, Response
from ..db import db
from app.models.planet import Planet

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    color = request_body["color"]
    description = request_body["description"]

    new_planet = Planet(name=name, color=color, description=description)
    db.session.add(new_planet)
    db.session.commit()
    response = new_planet.to_dict()
    return response, 201
@planets_bp.get("")
def get_all_planets():
    description_param = request.args.get("description")
    moon_param = request.args.get("moon")
    
    query = db.select(Planet)   
    
    if description_param:
        query =  db.select(Planet).where(Planet.description.like(f"%{description_param}%")).order_by(Planet.id)
    
    if moon_param:
        query = query.where(Planet.moon == int(moon_param))
    
    query = query.order_by(Planet.id)     
    # else:
    #     query = db.select(Planet).order_by(Planet.id)
        
    planets = db.session.scalars(query)
    planets_response = [planet.to_dict() for planet in planets]
    return planets_response

@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet_one(planet_id)
    # query = db.select(Planet).where(Planet.id == planet_id)
    # planet = db.session.scalar(query)


    return {
        "id": planet_id,
        "name": planet.name,
        "description": planet.description,
        "moon": planet.moon
    }

@planets_bp.put("/<planet_id>")
def update_planet(planet_id):
    planets = Planet.query.all()
    planet = validate_planet(planet_id, planets)
    request_body = request.get_json()

    planet.name= request_body["name"]
    planet.description = request_body["description"]
    planet.moon= request_body["moon"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@planets_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_planet_one(planet_id)
    db.session.delete(planet)
    db.session.commit()
    
    return Response(status=204, mimetype="application/json")


def validate_planet(planet_id, planets):
    # Narrow the errors - data error, type error
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Planet id {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message": f"Planet {planet_id} not found"}, 404))


def validate_planet_one(planet_id):

    try:
        planet_id = int(planet_id)
    except:
        response = {"message": f"planet {planet_id} invalid"}
        abort(make_response(response, 400))

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    if not planet:
        response = {"message": f"{planet_id} not found"}
        abort(make_response(response, 404))

    return planet