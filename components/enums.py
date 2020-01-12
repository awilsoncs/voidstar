from enum import auto, Enum


class Intention(Enum):
    NONE = auto()

    QUIT_GAME = auto()

    # Actions
    MELEE_ATTACK = auto()
    INTERACT_NEARBY = auto()
    SHOOT_NEARBY = auto()
    STEP_NORTH = auto()
    STEP_EAST = auto()
    STEP_WEST = auto()
    STEP_SOUTH = auto()

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