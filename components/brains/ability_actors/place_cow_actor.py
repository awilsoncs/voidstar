from dataclasses import dataclass

from components import Entity
from components.brains.ability_actors.place_thing_actor import PlaceThingActor
from content.cows import make_cow


@dataclass
class PlaceCowActor(PlaceThingActor):
    gold_cost: int = 100

    def make_thing(self, x: int, y: int) -> Entity:
        return make_cow(x, y)
