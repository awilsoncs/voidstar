from dataclasses import dataclass

import tcod

from components import TimedActor
from components.brains.brain import Brain
from components.enums import Intention
from engine import core


@dataclass
class PlayerDeadActor(Brain):
    timer_delay = TimedActor.REAL_TIME

    def act(self, scene):
        self.handle_key_event(scene)

    def handle_key_event(self, scene):
        key_event = core.get_key_event()
        if key_event:
            key_event = key_event.sym
            intention = DEAD_KEY_ACTION_MAP.get(key_event, None)
            if intention is not None:
                self.intention = intention


DEAD_KEY_ACTION_MAP = {
    tcod.event.K_BACKQUOTE: Intention.SHOW_DEBUG_SCREEN,
    tcod.event.K_ESCAPE: Intention.BACK
}
