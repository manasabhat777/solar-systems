"""Module which assumes that all the planets in the solar
   system are aligned.
"""

MODULE = 'foo'

def get_aligned_planets(planet_position):
    """Function to return the aligned planets
       in the solar system.
       This function assumes that all the planets
       in the solar system are aligned.
    """
    planets = []
    for name, position  in planet_position:
        planets.append(name)
    return set(planets)
