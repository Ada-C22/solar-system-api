from app import create_app, db
from app.models.planet import Planet

team_app = create_app()
with team_app.app_context():
    db.session.add(Planet(name="Mercury", description="The smallest and closest planet to the Sun", distance_from_sun=36000000)),
    db.session.add(Planet(name="Venus", description="Similar in size to Earth", distance_from_sun=67000000)),
    db.session.add(Planet(name="Earth", description="The only known planet to support life", distance_from_sun=93000000)),
    db.session.add(Planet(name="Mars", description="Known as the Red Planet", distance_from_sun=142000000)),
    db.session.add(Planet(name="Jupiter", description="The largest planet in the solar system", distance_from_sun=484000000)),
    db.session.add(Planet(name="Saturn", description="Famous for its beautiful ring system", distance_from_sun=886000000)),
    db.session.add(Planet(name="Uranus", description="An ice giant with a blue-green hue", distance_from_sun=1780000000)),
    db.session.add(Planet(name="Neptune", description="The farthest planet from the Sun", distance_from_sun=2800000000)),
    db.session.commit()
    # Add planets to solar-system-api db:
