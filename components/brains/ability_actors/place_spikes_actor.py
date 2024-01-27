from dataclasses import dataclass
from typing import Tuple, List

from components.brains.ability_actors.place_thing_actor import PlaceThingActor
from engine.components.component import Component
from content.spike_trap import make_spike_trap


@dataclass
class PlaceSpikesActor(PlaceThingActor):
    gold_cost: int = 5

    def make_thing(self, x: int, y: int) -> Tuple[int, List[Component]]:
        return make_spike_trap(x, y)
