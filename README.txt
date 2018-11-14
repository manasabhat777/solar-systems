What does your project do?
==================================
This project creates a command line application to print out planets that are aligned.
The application works for an arbitrary solar system. The planets in the
solar system will be define in a configuration file with the following format,

Example:

  system:
    - name: planet-A
      theta: 0
      radius: 1
      period: 20
    - name: planet-B
      theta: 0
      radius: 5
      period: 30
    - name: planet-C
      theta: 2
      radius: 10
      period: 60

The above configuration information should be stored/defined in .yaml format.
So each planet has a name, an initial angle (theta) given in radians, a radius
from the sun that it orbits, and length of time it takes to orbit the sun
(period). Assume that the orbit of each planet is a circle centered on the sun.

The position of each planet can be described by a radius and an angle. The
radius is constant, but the angle varies with time, i.e. at time 't' the angle
of a planet is given by,

  theta + 2 pi t / period

The application will not determine the alignments itself. Instead, the
application must be able to load a set of plugins at runtime that will determine
whether a particular configuration of planets is 'aligned' according to whatever
definition the plugin uses for alignment.

How is it set up?
==============================================
The application should support versions 2.7.x and 3.3.x (or greater) of python.
This application installation will install pyyaml python package for yaml parsing.


How is it used?
==============================================

Goto solar_system_script-0.1 folder and
install the package by executing:

sudo python setup.py install

Now you can run this application anywhere in your localhost!!!!!!
==============================================

The application must take arguments for the configuration file, a list of
plugins to load, and the time to calculate the alignment for. For example,

alignment.py --config config_samples/system.yaml --plugins plugin_samples/foo.py plugin_samples/bar.py plugin_samples/baz.py --time 1

where system.yaml has the planet configuration details .

Example of system.yaml is :
system:
    - name:planet-A
      theta: 0
      radius: 1
      period: 20
    - name:planet-B
      theta: 3.12
      radius: 5
      period: 30
    - name:planet-C
      theta: 3.14
      radius: 10
      period: 40

in the above commad line example:

--config is followed by the config file which is in yaml format and you can
pass any number of config files(.yaml files) separted by space.

example:
alignment.py --config config_samples/system.yaml config_samples/system1.yaml --plugins plugin_samples/foo.py plugin_samples/bar.py plugin_samples/baz.py --time 1

Similarly --plugins is followed by plugin samples which is .py file and you can pass any number of files separted by space.

As per physics :
   1 radian = 57.2958 degrees

Assumptions Made are :
--------------------------------------------
Internally, angles are mainited in deg. So we are assumimg that plugins will use
degree.After reaching 360 deg it will fallback to 0 degree.

minimum value for `time` is 0.

Plugin should follow belowing format :
--------------------------------------------
it should have a constant 'MODULE' declared in the global scope like :

MODULE = 'foo' where 'foo' is the name of the plugin.

and it should have a function named 'get_aligned_planets()' which takes list of
planet position and returns the aligned planet list.

and foo.py is a plugin and it assumes that all of the planets in the solar
system are aligned.

bar.py file is a plugin and it assumes and treats planets as aligned
if they are within 5 degrees of one another relative to the sun.

baz.py file is a plugin and it assumes and treats planets as aligned
if they are within 10 degrees of one another relative to the sun.

and the output will have the format,
--------------------------------------------
foo: planet-A, planet-C, planet-B
baz: planet-C, planet-B

first line in the output says that according to foo module all the planets are
aligned.

Second line says that according to baz module planet-C and planet-B are
aligned.

and according to bar none of the modules are aligned hence it did not print
anything in the output.

Necessary validation for inputs are done and it will be displayed in the
console when hits .
