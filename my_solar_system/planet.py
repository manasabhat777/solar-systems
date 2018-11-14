"""Module to define Planet and its properties.
"""

import math

class Planet:
    """Planet Class.
       This class contains the functionality to calculate the
       position of a planet in the solar system at time t.
    """
    def __init__(self, name, angle, radius, period):
        self._name = name
        # Unit for angle is degree
        # So convert radians to degree
        self._init_angle = (angle * 180) / math.pi
        self._radius = radius
        self._period = period
        self._position = None

    def upadate_position(self, time):
        """Function to update the position of the
           planet in the solar system at give time `time`
        """
        self._position = ((float(time)/float(self._period))*360)%360 + self._init_angle
