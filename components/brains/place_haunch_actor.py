from dataclasses import dataclass
from typing import Tuple, List

from components import Entity
from components.brains.place_thing_actor import PlaceThingActor
from content.farmsteads.defensive_walls import make_fence
from content.haunch import make_haunch
from engine.component import Component


@dataclass
class PlaceHaunchActor(PlaceThingActor):
    gold_cost: int = 5

    def make_thing(self, x: int, y: int) -> Entity:
        return make_haunch(x, y)
