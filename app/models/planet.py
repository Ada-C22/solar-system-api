class Planet:
  def __init__(self, id, name, description, diameter):
    self.id = id
    self.name = name
    self.description = description
    self.diameter = diameter

planets = [
  Planet(1, 'Earth', 'Earth is the fifth largest planet in our solar system and is the largest of the terrestrial planets', 7926),
  Planet(2, 'Jupiter', 'Jupiter is the fifth planet from the Sun and the largest in the Solar System', 86881),
  Planet(3, 'Saturn', 'Saturn is the sixth planet from the Sun and the second largest in the Solar System', 74897),
]