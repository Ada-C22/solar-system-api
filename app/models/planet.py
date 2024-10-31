from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from typing import Optional

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] 
    description: Mapped[str]
    number_moons: Mapped[Optional[int]]
    color: Mapped[Optional[str]]

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            number_moons=self.number_moons,
            color=self.color
        )

# class Planet: 
#     def __init__(self, id, name, description): 
#         self.id = id
#         self.name = name
#         self.description = description 
        

    
# planets = [
#     Planet(1, "Mars", "The red planet"),
#     Planet(2, "Earth", "The green planet"), 
#     Planet(3, "Jupiter", "The largest planet")
# ]
#pass