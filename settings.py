import os
# Font information
# If the game won't load or looks strange after changing the font,
# try changing FONT_GREYSCALE and FONT_ALTLAYOUT

# FONT = 'data\\fonts\\arial10x10.png'
DATA_DIR = 'data'
FONT = os.path.join('data', 'fonts', 'terminal16x16_gs_ro.png')

# actual size of the window
SCREEN_WIDTH = 90
SCREEN_HEIGHT = 50

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

# parameters for dungeon generator
ROOM_MAX_SIZE = 20
ROOM_MIN_SIZE = 10
MAX_ROOMS = 5
MAX_ROOM_MONSTERS = 10
MAX_ROOM_ITEMS = 2

FOV_ALGO = 'BASIC'
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 5
ENABLE_FOV = True

LEVEL_UP_BASE = 200
LEVEL_UP_FACTOR = 150
LEVEL_SCREEN_WIDTH = 40
CHARACTER_SCREEN_WIDTH = 30

# Persistence
MEMORY_ECHO = False
