from flask import Blueprint, abort, make_response, request
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
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)

    planets_response = [planet.to_dict() for planet in planets]
    return planets_response

def validate_planet(id):
    try: 
        id = int(id)
    except ValueError:
        abort(make_response({"message": f"Planet id {id} invalid"}, 400))

    abort(make_response({"message": f"Planet id {id} not found"}, 404))



