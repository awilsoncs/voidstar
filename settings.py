import os
import sys
import struct

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
        'autosave-enabled': True,
        'character-name': 'Sir Cameron',
        'grass-density': 2,
        'torch-radius': -1,
        'music-enabled': True,
        'color_background': '000000',
        'color_grass': '1f240a',
        'color_wall_tree':  '39571c',
        'color_normal_tree': 'a58c27',
        'color_gold': 'efac28',
        'color_white': 'efd8a1',
        'color_peasant': 'ab5c1c',
        'color_shadow': '183f39',
        'color_fire': 'ef692f',
        'color_straw': 'efb775',
        'color_dirt': 'a56243',
        'color_wood': '773421',
        'color_meat': '684c3c',
        'color_stone': '927e6a',
        'color_water': '276468',
        'color_fresh_blood': 'ef3a0c',
        'color_light_water': '3c9f9c',
        'color_hordeling': '9b1a0a',
        'color_blood': '550f0a'
    }
    with open(get_relative_path('options.yaml'), mode='w+') as file:
        yaml.dump(option_data_base, file)
    return option_data_base


try:
    with open('options.yaml') as options:
        option_data = yaml.load(options, Loader=yaml.FullLoader)
except FileNotFoundError:
    option_data = create_options_file()


AUTOSAVE = option_data['autosave-enabled']
GRASS_DENSITY = option_data['grass-density']
CHARACTER_NAME = option_data['character-name']
TORCH_RADIUS = option_data['torch-radius']
MUSIC_ENABLED = option_data['music-enabled']


# colors
def from_hex(hex_code):
    return struct.unpack('BBB', bytes.fromhex(hex_code))


BACKGROUND = from_hex(option_data['color_background'])
GRASS = from_hex(option_data['color_grass'])
WALL_TREE = from_hex(option_data['color_wall_tree'])
NORMAL_TREE = from_hex(option_data['color_normal_tree'])
GOLD = from_hex(option_data['color_gold'])
WHITE = from_hex(option_data['color_white'])
GABRIEL_2_1 = from_hex(option_data['color_peasant'])
SHADOW = from_hex(option_data['color_shadow'])
FIRE = from_hex(option_data['color_fire'])
STRAW = from_hex(option_data['color_straw'])
DIRT = from_hex(option_data['color_dirt'])
WOOD = from_hex(option_data['color_wood'])
MEAT = from_hex(option_data['color_meat'])
STONE = from_hex(option_data['color_stone'])
WATER = from_hex(option_data['color_water'])
FRESH_BLOOD = from_hex(option_data['color_fresh_blood'])
LIGHT_WATER = from_hex(option_data['color_light_water'])
HORDELING = from_hex(option_data['color_hordeling'])
BLOOD = from_hex(option_data['color_blood'])

# Nonconfigurable options
FONT = resource_path('resources/tiles.png')

# actual size of the window
SCREEN_WIDTH = 60
SCREEN_HEIGHT = 40

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
