from dataclasses import dataclass

import tcod

from components import TimedActor
from components.enums import Intention
from engine import core
from systems.utilities import set_intention


@dataclass
class PlayerDeadActor(TimedActor):
    timer_delay = TimedActor.REAL_TIME

    def act(self, scene):
        handle_key_event(scene, self.entity, DEAD_KEY_ACTION_MAP)


def handle_key_event(scene, entity_id, action_map):
    key_event = core.get_key_event()
    if key_event:
        key_event = key_event.sym
        intention = action_map.get(key_event, None)
        if intention is not None:
            set_intention(scene, entity_id, None, intention)


DEAD_KEY_ACTION_MAP = {
    tcod.event.K_BACKQUOTE: Intention.SHOW_DEBUG_SCREEN,
    tcod.event.K_ESCAPE: Intention.QUIT_GAME
}
