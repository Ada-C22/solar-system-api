class Planet:
    def __init__(self,id, name, description, moon):
        self.id = id
        self.name = name
        self.description = description
        self.moon = moon
        
planets = [
    Planet(1, "Mercury", "the smallest planet in the solar system and orbits closest to the Sun, with extreme temperatures ranging from 430°C (800°F) during the day to -180°C (-290°F) at night.", 0),
    Planet(2, "Venus", "the Sun and has a thick, toxic atmosphere composed mostly of carbon dioxide, creating a runaway greenhouse effect that makes it the hottest planet in the solar system with surface temperatures around 465°C (870°F", 0),
    Planet(3, "Earth", "Our home planet, the only known planet to harbor life",1),
    Planet(4,"Mars", "Red Planet due to its reddish appearance caused by iron oxide (rust) on its surface. It has a thin atmosphere composed mostly of carbon dioxide", 2 ),
    Planet(4, "Pluto", " filled with icy bodies and other small objects. Once considered the ninth planet in the solar system, it was reclassified as a dwarf planet in 2006 due to its size and the fact that it hasn’t cleared its orbit of other debris. Pluto has a rocky core surrounded by a mantle of water ice and a thin atmosphere of nitrogen, methane, and carbon monoxide.", 5),
    Planet(5, "Jupiter","is the largest planet in the solar system, a gas giant composed primarily of hydrogen and helium, known for its Great Red Spot—a massive storm larger than Earth", 92),
    Planet(6, "Saturn","sixth planet from the Sun and is best known for its extensive and stunning ring system, made mostly of ice and rock particles. It is a gas giant composed primarily of hydrogen and helium" , 146),
    Planet(7, "Uranus","is the seventh planet from the Sun, an ice giant with a blue-green color due to the presence of methane in its atmosphere. It is unique for rotating on its side, with an extreme axial tilt of about 98 degrees", 27 ),
    Planet(8, "Neptune", "is a blue ice giant, the eighth planet from the Sun. Known for strong winds and dark storms", 14),
    Planet(9, "Pluto", " a small, icy world in the outer solar system. It has a diverse, frozen landscape featuring a distinctive heart-shaped region", 5 ),
]
    