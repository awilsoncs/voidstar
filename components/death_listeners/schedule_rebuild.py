import logging
from dataclasses import dataclass

from components.death_listeners.death_listener import DeathListener
from components.house_structure import HouseStructure
from engine import constants


@dataclass
class ScheduleRebuild(DeathListener):
    """When this wall dies, set a delayed trigger to attempt to rebuild at the season reset."""
    root: int = constants.INVALID

    def on_die(self, scene):
        logging.info(f"{self.entity} scheduled rebuild")
        house_structure = scene.cm.get_one(HouseStructure, entity=self.root)
        if house_structure:
            house_structure.is_destroyed = True
