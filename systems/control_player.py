import tcod.event

from components.brain import Brain
from components.enums import Intention, ControlMode
from engine import core
from systems.utilities import set_intention


def run(scene) -> None:
    for brain in [b for b in scene.cm.get(Brain) if b.take_turn]:
        do_take_turn(scene, brain)


def do_take_turn(scene, brain: Brain) -> None:
    if brain and brain.control_mode == ControlMode.PLAYER:
        control_player(scene, brain.entity)


def control_player(scene, entity_id) -> None:
    """Get the player's input (if any) and dispatch the relevant action."""
    key_event = core.get_key_event()
    if key_event:
        key_event = key_event.sym
        if key_event in KEY_ACTION_MAP:
            intention = KEY_ACTION_MAP[key_event]
            set_intention(scene, entity_id, None, intention)


KEY_ACTION_MAP = {
    tcod.event.K_UP: Intention.STEP_NORTH,
    tcod.event.K_DOWN: Intention.STEP_SOUTH,
    tcod.event.K_RIGHT: Intention.STEP_EAST,
    tcod.event.K_LEFT: Intention.STEP_WEST,
    tcod.event.K_f: Intention.SHOOT_NEARBY,
    tcod.event.K_l: Intention.ACTIVATE_CURSOR,
    tcod.event.K_x: Intention.SHOW_DEBUG_SCREEN,
    tcod.event.K_SPACE: Intention.INTERACT_NEARBY,
    tcod.event.K_ESCAPE: Intention.QUIT_GAME
}
