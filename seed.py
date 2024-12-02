from app import create_app, db
from app.models.planet import Planet

my_app = create_app()
with my_app.app_context():
    db.session.add(Planet(name='Mercury',surface_area=28880,moons=0,distance_from_sun=35980,namesake='Roman god of travelers, aka Hermes.')),
    db.session.add(Planet(name='Venus',surface_area=177700,moons=0,distance_from_sun=67240,namesake='Roman goddess of love, aka Aphrodite.')),
    db.session.add(Planet(name='Earth',surface_area=196900,moons=1,distance_from_sun=92960,namesake='A variation on the word "ground" in several languages.')),
    db.session.add(Planet(name='Mars',surface_area=55910,moons=2,distance_from_sun=141600,namesake='Roman god of war, aka Ares.')),
    db.session.add(Planet(name='Jupiter',surface_area=23710000,moons=79,distance_from_sun=483300,namesake='King of the Roman gods, aka Zeus.')),
    db.session.add(Planet(name='Saturn',surface_area=16490000,moons=62,distance_from_sun=890700,namesake='Jupiter''s father and titan, aka Chronos.')),
    db.session.add(Planet(name='Uranus',surface_area=3121000,moons=27,distance_from_sun=1787000,namesake='Greek personification of the sky or heavens, aka Caelus.')),
    db.session.add(Planet(name='Neptune',surface_area=2941000,moons=14,distance_from_sun=2798000,namesake='Roman god of the sea, aka Poseidon.'))
    db.session.commit()