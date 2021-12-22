from dataclasses import dataclass
from typing import Tuple, List

import tcod

from components import Coordinates
from components.actors.energy_actor import EnergyActor
from components.animation_effects.blinker import AnimationBlinker
from components.enums import Intention
from components.player_controllers.place_thing_actor import PlaceThingActor
from content.farmsteads.defensive_walls import make_fence
from content.terrain.saplings import make_sapling
from engine import constants, core
from engine.component import Component


@dataclass
class PlaceFenceActor(PlaceThingActor):
    gold_cost: int = 5

    def make_thing(self, x: int, y: int) -> Tuple[int, List[Component]]:
        return make_fence(x, y)
