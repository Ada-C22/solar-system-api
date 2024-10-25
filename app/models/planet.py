from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    surface_area: Mapped[int]
    moons: Mapped[int]
    distance_from_sun: Mapped[int]
    namesake: Mapped[str]

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            surface_area=self.surface_area,
            moons=self.moons,
            distance_from_sun=self.distance_from_sun,
            namesake=self.namesake
        )

# class Planet:
#     def __init__(self, id, name, description, distance_from_earth):
#         self.id = id
#         self.name = name
#         self. description = description
#         self.distance_from_earth = distance_from_earth

#     def to_dict(self):
#         return dict(
#             id=self.id,
#             name=self.name,
#             description=self.description,
#             distance_from_earth=self.distance_from_earth
#         )

# planets = [
#     Planet(1, "Mercury", "smallest, rocky", 216.3),
#     Planet(2, "Venus", "hot, thick atmostphere", 259.71),
#     Planet(3, "Earth", "only known planet with life", 0),
#     Planet(4, "Mars", "dusty, red, cold", 399.58),
#     Planet(5, "Jupiter", "largest, gas giant", 965.52),
#     Planet(6, "Saturn", "ringed, gas giant", 1652.48),
#     Planet(7, "Uranus", "ice giant, tilted axis", 3154.91),
#     Planet(8, "Neptune", "farthest, ice giant", 4685.02),
#     Planet(9, "Pluto", "very cold, five moons", 7523.53)
# ]
