class Planet:
    def __init__(self, id, name, description, distance_from_earth):
        self.id = id
        self.name = name
        self. description = description
        self.distance_from_earth = distance_from_earth

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            distance_from_earth=self.distance_from_earth
        )

planets = [
    Planet(1, "Mercury", "smallest, rocky", 216.3),
    Planet(2, "Venus", "hot, thick atmostphere", 259.71),
    Planet(3, "Earth", "only known planet with life", 0),
    Planet(4, "Mars", "dusty, red, cold", 399.58),
    Planet(5, "Jupiter", "largest, gas giant", 965.52),
    Planet(6, "Saturn", "ringed, gas giant", 1652.48),
    Planet(7, "Uranus", "ice giant, tilted axis", 3154.91),
    Planet(8, "Neptune", "farthest, ice giant", 4685.02),
    Planet(9, "Pluto", "very cold, five moons", 7523.53)
]


