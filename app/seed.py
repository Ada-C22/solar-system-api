from app import create_app, db
from app.models.planets import Planet

my_app = create_app()
with my_app.app_context():
    db.session.add(Planet(name="Mercury", description="terrestrial planet", size=1516)),
    db.session.add(Planet(name="Venus", description="Earth's twin", size=3760.4)),
    db.session.add(Planet(name="Earth", description="livable planet", size=3958.8)),
    db.session.add(Planet(name="Mars", description="the red planet", size=2106.1)),
    db.session.add(Planet(name="Jupiter", description="the largest planet", size=43441)),
    db.session.add(Planet(name="Saturn", description="the second largest planet", size=36184)),
    db.session.add(Planet(name="Uranus", description="the icy planet", size=15759)),
    db.session.add(Planet(name="Neptune", description="the blue planet", size=15299)),
    db.session.add(Planet(name="Pluto", description="the forgotten planet", size=1473)),
    db.session.commit()