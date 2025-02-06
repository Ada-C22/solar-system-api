from flask import Blueprint, abort, make_response, request, Response
from app.models.planet import Planet
from ..db import db

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.get("")
def get_all_planets():
  query = db.select(Planet)

  description_param = request.args.get("description")
  smallest_diameter_param = request.args.get("smallest_diameter")
  largest_diameter_param = request.args.get("largest_diameter")

  if description_param:
    query = query.where(Planet.description.ilike(f"%{description_param}%"))
  if smallest_diameter_param:
    query = query.where(Planet.diameter < largest_diameter_param)
  if largest_diameter_param:
    query = query.where(Planet.diameter > smallest_diameter_param)

  planets = db.session.scalars(query.order_by(Planet.id))

  planet_response = []
  for planet in planets:
    planet_response.append(
        {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "diameter": planet.diameter,
        }
    )
  return planet_response

@planet_bp.get("/<planet_id>")
def get_one_planet(planet_id):
  planet = validate_planet(planet_id)  

  return {
    "name": planet.name,
    "description": planet.description,
    "diameter": planet.diameter,
  }

@planet_bp.put("/<planet_id>")
def update_planet(planet_id):
  planet = validate_planet(planet_id)
  request_body = request.get_json()

  planet.name = request_body["name"]
  planet.description = request_body["description"]
  planet.diameter = request_body["diameter"]

  db.session.commit()

  return Response(status=204, mimetype="application/json")

@planet_bp.post("")
def create_planet():
  request_body = request.get_json()
  name = request_body["name"]
  description = request_body["description"]
  diameter = request_body["diameter"]

  new_planet = Planet(name=name, description=description, diameter=diameter)
  db.session.add(new_planet)
  db.session.commit()

  response = {
    "id": new_planet.id,
    "name": new_planet.name,
    "description": new_planet.description,
    "diameter": new_planet.diameter,
  }

  return response, 201

@planet_bp.delete("/<planet_id>")
def delete_planet(planet_id):
  planet = validate_planet(planet_id)
  db.session.delete(planet)
  db.session.commit()

  return Response(status=204, mimetype="application/json")

def validate_planet(planet_id):
  try:
    planet_id = int(planet_id)
  except:
    response = {"message": f"Planet {planet_id} invalid"}
    abort(make_response(response, 400))

  query = db.select(Planet).where(Planet.id == planet_id)
  planet = db.session.scalar(query)

  if not planet:
    response = {"message": f"Planet {planet_id} not found"}
    abort(make_response(response, 404))

  return planet