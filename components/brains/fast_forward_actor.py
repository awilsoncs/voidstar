import logging
from dataclasses import dataclass

import tcod

from components.brains.temporary_brain import TemporaryBrain
from components.enums import Intention
from engine import core


@dataclass
class FastForwardBrain(TemporaryBrain):
    def act(self, scene):
        self.handle_key_event(scene, KEY_ACTION_MAP)

    def handle_key_event(self, scene, action_map):
        key_event = core.get_key_event()
        if key_event:
            self._log_debug(f"received input {key_event}")
            key_code = key_event.sym
            intention = action_map.get(key_code, None)
            self._log_debug(f"translated {key_event} -> {intention}")
            if intention == Intention.BACK:
                self.back_out(scene)
                return
        else:
            self.intention = Intention.DALLY


KEY_ACTION_MAP = {
    tcod.event.K_PERIOD: Intention.DALLY,
    tcod.event.K_ESCAPE: Intention.BACK
}
