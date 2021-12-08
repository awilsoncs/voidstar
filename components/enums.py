from enum import auto, Enum


class Intention(Enum):
    NONE = auto()

    BACK = auto()

    # Actions
    MELEE_ATTACK = auto()
    THWACK = auto()
    SHOOT = auto()
    STEP_NORTH = auto()
    STEP_EAST = auto()
    STEP_WEST = auto()
    STEP_SOUTH = auto()
    STEP_SOUTH_EAST = auto()
    STEP_SOUTH_WEST = auto()
    STEP_NORTH_EAST = auto()
    STEP_NORTH_WEST = auto()
    DALLY = auto()
    FAST_FORWARD = auto()

    ACTIVATE_CURSOR = auto()
    REPORT_CURSOR = auto()
    REPORT_LOCATION = auto()
    KILL_CURSOR = auto()

    # Screen Control
    SHOW_DEBUG_SCREEN = auto()


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
