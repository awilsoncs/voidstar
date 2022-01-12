from dataclasses import dataclass

from components import Entity
from components.brains.ability_actors.place_thing_actor import PlaceThingActor
from content.allies.knights import make_knight


@dataclass
class HireKnightActor(PlaceThingActor):
    gold_cost: int = 100

    def make_thing(self, x: int, y: int) -> Entity:
        return make_knight(x, y)
