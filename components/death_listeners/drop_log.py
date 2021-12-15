from dataclasses import dataclass

from components import Coordinates
from components.death_listeners.death_listener import DeathListener
from content.getables.fallen_log import make_fallen_log


@dataclass
class DropFallenLog(DeathListener):
    """Drop gold when the owner dies."""

    def on_die(self, scene):
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        scene.cm.add(*make_fallen_log(coords.x, coords.y)[1])
