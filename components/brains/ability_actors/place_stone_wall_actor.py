from dataclasses import dataclass
from typing import Tuple, List

from components.brains.ability_actors.place_thing_actor import PlaceThingActor
from content.farmsteads.defensive_walls import make_stone_wall
from components.base_components.component import Component


@dataclass
class PlaceStoneWallActor(PlaceThingActor):
    gold_cost: int = 10

    def make_thing(self, x: int, y: int) -> Tuple[int, List[Component]]:
        return make_stone_wall(x, y)
