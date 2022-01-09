import logging
from dataclasses import dataclass

from components.death_listeners.death_listener import DeathListener
from engine import constants


@dataclass
class Stomach(DeathListener):
    contents: int = constants.INVALID

    def on_die(self, scene):
        logging.debug(f"EID#{self.entity}::Stomach on_die triggered, dumping contents")
        if self.contents == constants.INVALID:
            logging.debug(f"EID#{self.entity}::Stomach nothing to dump")
            return

        logging.debug(f"EID#{self.entity}::Stomach dumping {self.contents}")
        scene.cm.unstash_entity(self.contents)

    def clear(self, scene):
        if self.contents == constants.INVALID:
            return

        logging.debug(f"EID#{self.entity}::Stomach clearing contents {self.contents}")
        scene.cm.drop_stashed_entity(self.contents)
        self.contents = constants.INVALID
