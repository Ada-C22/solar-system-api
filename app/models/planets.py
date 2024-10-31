from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

# New Code added
class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    distance_from_sun: Mapped[float]

    def get_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        "description": self.description,
        "distance_from_sun": self.distance_from_sun
    }
        
