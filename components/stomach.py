import logging
from dataclasses import dataclass

from components.events.die_events import DeathListener
from engine import constants


@dataclass
class Stomach(DeathListener):
    contents: int = constants.INVALID

    def on_die(self, scene):
        self._log_debug(f"on_die triggered, dumping contents")
        if self.contents == constants.INVALID:
            logging.debug(f"EID#{self.entity}::Stomach nothing to dump")
            return

        self._log_debug(f"dumping {self.contents}")
        scene.cm.unstash_entity(self.contents)

    def clear(self, scene):
        if self.contents == constants.INVALID:
            return

        self._log_debug(f"clearing contents {self.contents}")
        scene.cm.drop_stashed_entity(self.contents)
        self.contents = constants.INVALID
