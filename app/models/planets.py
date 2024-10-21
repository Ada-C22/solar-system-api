

class Planet:
    def __init__(self, id, name, description, size):
        self.id = id
        self.name = name
        self.desciption = description
        self.size = size


planet_list = [
    Planet(21, "Mercury", "hottest", "56325"),
    Planet(32, "Saturn", "with_rings", "653645"),
    Planet(45, "Venus", "small", "657436"),
    Planet(56, "Mars", "lively", "765347"),
    Planet(78, "Pluto", "non_existing", "763787"),
    Planet(89, "Jupiter", "biggest", "98765")
]


