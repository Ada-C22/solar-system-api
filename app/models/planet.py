class Planet:
    def __init__(self, id, name, description, size_dia_km):
        self.id = id
        self.name = name
        self.description = description
        self.size = size_dia_km

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            desc=self.description,
            size=self.size
        )
    
planets = [
    Planet(1,"some_planet", "rocky, no signs of life", 100),
    Planet(2, "Earth", "with lifeforms, water and land", 5000),
    Planet(3, "Pluto", "still a planet", 200)
]