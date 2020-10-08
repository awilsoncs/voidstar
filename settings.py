import os
import sys

import yaml


def resource_path(relative_path):
    try:
        # required for accessing resources within pyinstaller executable
        # noinspection PyProtectedMember,PyUnresolvedReferences
        base_path = sys._MEIPASS
    except AttributeError:
        # sys._MEIPASS only exists within python compiled for pyinstaller executables
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


def get_relative_path(relative_path):
    base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


def create_options_file():
    option_data_base = {
        'screen-width': 90,
        'screen-height': 50,
        'grass-density': 2,
        'lakes-min': 1,
        'lakes-max': 4,
        'lake-proliferation': .2,
        'copse-min': 10,
        'copse-max': 20,
        'copse-proliferation': .05,
        'character-name': 'Sir Chauncey',
        'spawn-min': 1,
        'spawn-max': 6,
        'torch-radius': -1
    }
    with open(get_relative_path('options.yaml'), mode='w+') as file:
        yaml.dump(option_data_base, file)
    return option_data_base


try:
    with open('options.yaml') as options:
        option_data = yaml.load(options, Loader=yaml.FullLoader)
except FileNotFoundError:
    option_data = create_options_file()


# actual size of the window
SCREEN_WIDTH = option_data['screen-width']
SCREEN_HEIGHT = option_data['screen-height']
GRASS_DENSITY = option_data['grass-density']
LAKES_MIN = option_data['lakes-min']
LAKES_MAX = option_data['lakes-max']
LAKE_PROLIFERATION = option_data['lake-proliferation']
COPSE_MIN = option_data['copse-min']
COPSE_MAX = option_data['copse-max']
COPSE_PROLIFERATION = option_data['copse-proliferation']
CHARACTER_NAME = option_data['character-name']
SPAWN_MIN = option_data['spawn-min']
SPAWN_MAX = option_data['spawn-max']
TORCH_RADIUS = option_data['torch-radius']

# Nonconfigurable options
FONT = resource_path('tiles.png')

# size of the map
MAP_WIDTH = SCREEN_WIDTH - 25
MAP_HEIGHT = SCREEN_HEIGHT

# sizes and coordinates relevant for the GUI
BAR_WIDTH = 20
PANEL_HEIGHT = 7
PANEL_Y = SCREEN_HEIGHT - PANEL_HEIGHT
MSG_X = BAR_WIDTH + 2
MSG_WIDTH = SCREEN_WIDTH - BAR_WIDTH - 2
MSG_HEIGHT = PANEL_HEIGHT - 1
INVENTORY_WIDTH = 50

FOV_ALGO = 'BASIC'
FOV_LIGHT_WALLS = True
SPAWN_FREQUENCY = 15
