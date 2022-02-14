from dataclasses import dataclass

from components.brains.ability_actors.place_thing_actor import PlaceThingActor
from content.bomb import make_bomb
from engine.types import Entity


@dataclass
class PlaceBombActor(PlaceThingActor):
    gold_cost: int = 10

    def make_thing(self, x: int, y: int) -> Entity:
        return make_bomb(x, y)
