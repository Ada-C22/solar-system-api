class Planet:
    def __init__(self, id, name, description, distance_from_sun):
        self.id = id
        self.name = name
        self.description = description
        self.distance_from_sun = distance_from_sun

planets =[
    Planet(1, "Mercury", "smallest and hottest planet", 57.9),
    Planet(2, "Venus", "second planet from the sun", 108.2),
    Planet(3, "Earth", "our home planet", 149.6),
    Planet(4, "Mars", "the red planet", 227.9),
    Planet(5, "Jupiter", "largest planet in the solar system", 778.3),
    Planet(6, "Saturn", "has beautiful rings", 1437.0),
    Planet(7, "Uranus", "rotates on its side", 2871.0),
    Planet(8, "Neptune", "farthest planet from the sun", 4497.1)
    ]