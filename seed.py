from app import create_app, db
from app.models.planet import Planet

my_app = create_app()
with my_app.app_context():
    db.session.add(Planet(name="Mercury", description="The smallest planet",number_moons=0,color="Gray")),
    db.session.add(Planet(name="Venus", description="Our closest neighbor",number_moons=0,color="Yellowish")),
    db.session.add(Planet(name="Earth", description="The green planet",number_moons=1,color="Blue")),
    db.session.add(Planet(name="Mars", description="The red planet",number_moons=2,color="Red")),
    db.session.add(Planet(name="Jupiter", description="The largest planet",number_moons=95,color="Yellow")),
    db.session.add(Planet(name="Saturn", description="A gas giant",number_moons=146,color="Yellow")),
    db.session.add(Planet(name="Uranus", description="A sideways planet",number_moons=28,color="Blue",)),
    db.session.add(Planet(name="Neptune", description="Has super sonic winds",number_moons=16,color="Blue")),
    db.session.add(Planet(name="Pluto", description="The dwarf planet",number_moons=0,color="Red")),
    db.session.commit()