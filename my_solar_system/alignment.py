#!/usr/bin/env python

"""
Module that accepts and parses command line input
like python alignment.py --config system.yaml --plugins ~/foo.py ~/bar.py ~/baz.py --time 10
"""

import argparse
import imp
import os
import sys
import yaml

from my_solar_system.solar_system import SolarSystem

# argparse is a more convenient, flexible,
# and powerful library for parsing command-line args.
# it is better for following:
# handling positional arguments
# supporting sub-commands
# allowing alternative option prefixes like + and /
# handling zero-or-more and one-or-more style arguments
# producing more informative usage messages
# providing a much simpler interface for custom types and actions.
parser = argparse.ArgumentParser(description='Planet input parser')
parser.add_argument('--config',
                    nargs='*',
                    default=[],
                    help='Config file to use.'
                   )

parser.add_argument('--plugins',
                    nargs='*',
                    default=[],
                    help='Plugins to calculate the planet alignments.'
                   )

parser.add_argument('--time',
                    default=None,
                    help='time at which planet position needs to calculated.'
                   )

def parse_config(config_files):
    """Function to parse the yaml format config file.

        :Parameters:
            - `config_file`: yaml format config file.

        :Return:
            - A dictionaty containing planet details.
              Example:{'system': [{'theta': 0, 'radius': 1, 'name': 'planet-A', 'period': 20}]}
    """

    systems_list = []
    for config_file in config_files:
        systems = None
        with open(config_file, 'r') as stream:
            try:
                #PyYAML is a YAML parser and emitter for the Python programming language.
                systems = yaml.load(stream.read())
            except yaml.composer.ComposerError as exp:
                print("Config syntex error : " + str(exp))
                sys.exit(0)
            except Exception as exp:
                print("Config syntex error : " + str(exp))
                sys.exit(0)
            systems_list.append(systems)
    return systems_list

def execute_plugins(plugins):
    """Function to parse the plugins which decides the planet alignment
       and load the module defined inside the plugin.

        :Parameters:
            - `plugins`: list of plugin files having planet alignment calculation definitions.
            - `solar_sys`: object refering to SolarSystem class
        :Return:
            - print aligned planet names.
    """
    for plugin_src in plugins:

        if not os.path.isfile(plugin_src):
            print("Plugin not found : " + plugin_src)
            continue

        path, fname = os.path.split(plugin_src)
        module_name, ext = os.path.splitext(fname)
        try:
            plugin = imp.load_source(module_name, plugin_src)
        except SyntaxError as exp:
            print("Plugin syntax error : " + str(exp))
            continue
        except Exception as exp:
            print("Failed to import : " + str(exp))
            continue

        #print all the alinged planet as per plugin
        solar_sys.print_aligned_planets(plugin)

if __name__ == '__main__':
    args = parser.parse_args()

    #Check whether all the inputs are given or not
    if not args.config or not args.plugins or not args.time:
        parser.print_help()
        sys.exit(0)
    for configfile in args.config:
        if not os.path.isfile(configfile):
            print("Config file not found : " + configfile)
            sys.exit(0)

    if int(args.time) < 0:
        print("Time cannot be negative value")
        sys.exit(0)
    # Parse yaml config file
    config_systems = parse_config(args.config)


    #Instantiate SolarSystem class
    solar_sys = SolarSystem(int(args.time))

    #Add the planet details to solar_system
    for config_system in config_systems:
        for planet in config_system['system']:
            solar_sys.add_planet(planet['name'],
                                 planet['theta'],
                                 planet['radius'],
                                 planet['period']
                                )

    #load the required plugins
    execute_plugins(args.plugins)
