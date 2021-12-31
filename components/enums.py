from enum import auto, Enum


class Intention(Enum):
    NONE = auto()

    BACK = auto()

    # Actions
    NEXT_ABILITY = auto()
    PREVIOUS_ABILITY = auto()
    USE_ABILITY = auto()

    STEP_NORTH = auto()
    STEP_EAST = auto()
    STEP_WEST = auto()
    STEP_SOUTH = auto()
    STEP_SOUTH_EAST = auto()
    STEP_SOUTH_WEST = auto()
    STEP_NORTH_EAST = auto()
    STEP_NORTH_WEST = auto()
    DALLY = auto()
    SHOW_DEBUG_SCREEN = auto()
    SHOW_HELP = auto()


class ControlMode(Enum):
    MONSTER = 'monster'
    PLAYER = 'player'
    CURSOR = 'cursor'
    WANDER = 'wander'
    DEAD_PLAYER = 'dead_player'
    FOLLOW_PATH = 'follow_path'
    CALENDER = 'calendar'


class FactionType(Enum):
    NONE = 'none'
    MONSTER = 'monster'
    PEASANT = 'peasant'
