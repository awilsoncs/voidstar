import tcod.event

from components.brain import Brain
from components.enums import Intention, ControlMode
from engine import core
from systems.utilities import set_intention


def run(scene) -> None:
    for brain in [b for b in scene.cm.get(Brain) if b.take_turn]:
        do_take_turn(scene, brain)


def do_take_turn(scene, brain: Brain) -> None:
    if brain and brain.control_mode is ControlMode.PLAYER:
        handle_key_event(scene, brain.entity, KEY_ACTION_MAP)
    if brain and brain.control_mode is ControlMode.DEAD_PLAYER:
        handle_key_event(scene, brain.entity, DEAD_KEY_ACTION_MAP)


def handle_key_event(scene, entity_id, action_map):
    key_event = core.get_key_event()
    if key_event:
        key_event = key_event.sym
        intention = action_map.get(key_event, None)
        set_intention(scene, entity_id, None, intention)


DEAD_KEY_ACTION_MAP = {
    tcod.event.K_l: Intention.ACTIVATE_CURSOR,
    tcod.event.K_x: Intention.SHOW_DEBUG_SCREEN,
    tcod.event.K_ESCAPE: Intention.QUIT_GAME
}

KEY_ACTION_MAP = {
    tcod.event.K_KP_1: Intention.STEP_SOUTH_WEST,
    tcod.event.K_KP_2: Intention.STEP_SOUTH,
    tcod.event.K_KP_3: Intention.STEP_SOUTH_EAST,
    tcod.event.K_KP_4: Intention.STEP_WEST,
    tcod.event.K_KP_5: Intention.DALLY,
    tcod.event.K_KP_6: Intention.STEP_EAST,
    tcod.event.K_KP_7: Intention.STEP_NORTH_WEST,
    tcod.event.K_KP_8: Intention.STEP_NORTH,
    tcod.event.K_KP_9: Intention.STEP_NORTH_EAST,

    tcod.event.K_UP: Intention.STEP_NORTH,
    tcod.event.K_DOWN: Intention.STEP_SOUTH,
    tcod.event.K_RIGHT: Intention.STEP_EAST,
    tcod.event.K_LEFT: Intention.STEP_WEST,

    tcod.event.K_l: Intention.ACTIVATE_CURSOR,
    tcod.event.K_x: Intention.SHOW_DEBUG_SCREEN,
    tcod.event.K_SPACE: Intention.INTERACT_NEARBY,
    tcod.event.K_ESCAPE: Intention.QUIT_GAME
}
