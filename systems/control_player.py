import tcod.event

from components.brains.brain import Brain
from components.enums import Intention, ControlMode
from components.events.turn_event import TurnEvent
from components.states.dizzy_state import DizzyState
from content.states import dizzy_animation
from engine import core, PLAYER_ID
from systems.utilities import set_intention


def run(scene) -> None:
    turn = scene.cm.get_one(TurnEvent, entity=PLAYER_ID)
    if turn:
        brain = scene.cm.get_one(Brain, entity=PLAYER_ID)
        do_take_turn(scene, brain)


