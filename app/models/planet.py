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

    @classmethod
    def from_dict(cls, planet_data):
        return cls(
            name=planet_data["name"],
            surface_area=planet_data["surface_area"],
            moons=planet_data["moons"],
            distance_from_sun=planet_data["distance_from_sun"],
            namesake=planet_data["namesake"]
        )
