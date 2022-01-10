from enum import Enum


class Intention(str, Enum):
    NONE = 'none'

    BACK = 'back'

    # Actions
    NEXT_ABILITY = 'next_ability'
    PREVIOUS_ABILITY = 'previous_ability'
    USE_ABILITY = 'use_ability'

    STEP_NORTH = 'step_north'
    STEP_EAST = 'step_east'
    STEP_WEST = 'step_west'
    STEP_SOUTH = 'step_south'
    STEP_SOUTH_EAST = 'step_south_east'
    STEP_SOUTH_WEST = 'step_south_west'
    STEP_NORTH_EAST = 'step_north_east'
    STEP_NORTH_WEST = 'step_north_west'
    DALLY = 'dally'
    SHOW_DEBUG_SCREEN = 'show_debug'
    SHOW_HELP = 'show_help'


class ControlMode(str, Enum):
    MONSTER = 'monster'
    PLAYER = 'player'
    CURSOR = 'cursor'
    WANDER = 'wander'
    DEAD_PLAYER = 'dead_player'
    FOLLOW_PATH = 'follow_path'
    CALENDER = 'calendar'


class FactionType(str, Enum):
    NONE = 'none'
    MONSTER = 'monster'
    PEASANT = 'peasant'
