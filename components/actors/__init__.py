from components.enums import Intention

VECTOR_STEP_MAP = {
    (0, -1): Intention.STEP_NORTH,
    (-1, -1): Intention.STEP_NORTH,
    (1, -1): Intention.STEP_NORTH,
    (0, 1): Intention.STEP_SOUTH,
    (0, 0): Intention.NONE,
    (1, 1): Intention.STEP_SOUTH,
    (-1, 1): Intention.STEP_SOUTH,
    (1, 0): Intention.STEP_EAST,
    (-1, 0): Intention.STEP_WEST,
    (1, -1): Intention.STEP_NORTH_EAST,
    (-1, -1): Intention.STEP_NORTH_WEST,
    (1, 1): Intention.STEP_SOUTH_EAST,
    (-1, 1): Intention.STEP_SOUTH_WEST
}
STEPS = [
    Intention.NONE,
    Intention.STEP_NORTH,
    Intention.STEP_SOUTH,
    Intention.STEP_EAST,
    Intention.STEP_WEST
]