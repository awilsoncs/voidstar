from dataclasses import dataclass

from components import Coordinates
from components.death_listeners.death_listener import DeathListener
from content.gold import make_gold_nugget
from engine.component import Component


@dataclass
class DropGold(DeathListener):
    """Drop gold when the owner dies."""

    def on_die(self, scene):
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        scene.cm.add(*make_gold_nugget(coords.x, coords.y)[1])
