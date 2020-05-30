import tcod.event

from components.actions.thwack_action import ThwackAction
from components.brain import Brain
from components.enums import Intention, ControlMode
from components.events.turn_event import TurnEvent
from engine import core, PLAYER_ID
from systems.utilities import set_intention


def run(scene) -> None:
    turn = scene.cm.get_one(TurnEvent, entity=PLAYER_ID)
    if turn:
        brain = scene.cm.get_one(Brain, entity=PLAYER_ID)
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
        if intention is not None:
            set_intention(scene, entity_id, None, intention)
        else:
            # new event-based actions
            if key_event is tcod.event.K_SPACE:
                scene.cm.add(ThwackAction(entity=entity_id))


DEAD_KEY_ACTION_MAP = {
    tcod.event.K_l: Intention.ACTIVATE_CURSOR,
    tcod.event.K_BACKQUOTE: Intention.SHOW_DEBUG_SCREEN,
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

    tcod.event.K_z: Intention.STEP_SOUTH_WEST,
    tcod.event.K_x: Intention.STEP_SOUTH,
    tcod.event.K_c: Intention.STEP_SOUTH_EAST,
    tcod.event.K_a: Intention.STEP_WEST,
    tcod.event.K_s: Intention.DALLY,
    tcod.event.K_d: Intention.STEP_EAST,
    tcod.event.K_q: Intention.STEP_NORTH_WEST,
    tcod.event.K_w: Intention.STEP_NORTH,
    tcod.event.K_e: Intention.STEP_NORTH_EAST,

    tcod.event.K_UP: Intention.STEP_NORTH,
    tcod.event.K_DOWN: Intention.STEP_SOUTH,
    tcod.event.K_RIGHT: Intention.STEP_EAST,
    tcod.event.K_LEFT: Intention.STEP_WEST,

    tcod.event.K_l: Intention.ACTIVATE_CURSOR,
    tcod.event.K_BACKQUOTE: Intention.SHOW_DEBUG_SCREEN,
    tcod.event.K_ESCAPE: Intention.QUIT_GAME
}
