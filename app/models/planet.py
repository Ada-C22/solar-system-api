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

