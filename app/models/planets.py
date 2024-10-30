from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

# New Code added
class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    distance_from_sun: Mapped[int]

    def get_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        "description": self.description,
        "distance_from_sun": self.distance_from_sun
    }
        
# planets = [
#     Planet(1, "Mercury", "Smallest, closest to the Sun, extreme temperatures.", 57.9),
#     Planet(2, "Venus", "Hot, toxic atmosphere, Earth's size, rotates backward.", 108.2),
#     Planet(3, "Earth", "Supports life, water in all forms, protective atmosphere.", 149.6),
#     Planet(4, "Mars", "Red planet, potential for human exploration, largest volcano.", 227.9),
#     Planet(5, "Jupiter", "Largest, gas giant, famous Great Red Spot, many moons.", 778.3),
#     Planet(6, "Saturn", "Known for rings, gas giant, over 80 moons.", 1427),
#     Planet(7, "Uranus", "Ice giant, tilted, blue-green due to methane.", 2871),
#     Planet(8, "Neptune", "Farthest, blue, strongest winds.", 4495)
# ]