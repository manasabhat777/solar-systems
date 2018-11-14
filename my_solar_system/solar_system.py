"""Module to define the SolarSystem class
   and its properties.
"""

import sys

from planet import Planet

class SolarSystem:

    """SolarSystem class.
    This class contains the functionality to add a planet
    and display the aligined planets in the solar system.
    """

    def __init__(self, time):
        self._time = time
        self._planets = []

    def add_planet(self, name, angle, radius, period):
        """Function to add a planet to the solar system.

        :Parameters:
            - `name`: name of the planet
            - `angle`: initial angle given in radians
            - `radius`: perpendicular distance from sun
            - `period`: length of time planet takes to orbit the sun

        :Return:
            - list of planets
        """
        tmp_planet = Planet(name, angle, radius, period)
        tmp_planet.upadate_position(self._time)

        self._planets.append(tmp_planet)

    def print_aligned_planets(self, plugin):

        """Display the names of aligned planets
           based on the definition defined in plugin.
        """
        planet_positon = []

        for planet in self._planets:
            planet_positon.append((planet._name, planet._position))

        aligned_planets = plugin.get_aligned_planets(planet_positon)
        if aligned_planets:
            sys.stdout.write(plugin.MODULE + ': ')
            add_delimitor = False
            for planet in aligned_planets:
                if add_delimitor:
                    sys.stdout.write(", ")

                sys.stdout.write(planet)
                add_delimitor = True
            sys.stdout.write('\n')
