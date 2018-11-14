"""Module to calcuate the aligned planets.
"""

MODULE = 'baz'

def get_aligned_planets(planet_position):
    """ Function to calculate the aligned planets.
        :Parameters:
            - `planet_position`: planet position in the orbit
        :Return:
            - list of aligned planets
    """
    # Assumed that each window is 5 degree
    # and granular unit for the increment is 1 degree.
    aligned_groups = []
    alignment_window = 10
    wind_beg = 0
    wind_end = wind_beg + alignment_window
    resolution = 1

    while True:

        aligned = []
        for name, position in planet_position:
            if position >= wind_beg and position <= wind_end:
                aligned.append(name)
        wind_beg = wind_beg + resolution
        wind_end = wind_beg + alignment_window
        if aligned and len(aligned) != 1:
            aligned_groups.append(aligned)

        if wind_beg == 351:
            break

    wind_end = wind_end

    while wind_end <= 370:

        aligned = []
        for name, position in planet_position:
            if (position - 10) % 360 >= (wind_beg - 10) % 360 and \
                    (position - 10) % 360 <= (wind_end - 10) % 360:
                aligned.append(name)

        wind_beg = wind_beg + resolution
        wind_end = wind_beg + alignment_window

        if aligned and len(aligned) != 1:
            aligned_groups.append(aligned)

    unique_list_aligned_planets = [list(x) for x in set(tuple(x) for x in aligned_groups)]
    alinged_planets = [planet for sublist in unique_list_aligned_planets for planet in sublist]
    return set(alinged_planets)
