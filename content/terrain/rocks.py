import random
from typing import List, Tuple

from components import Appearance, Coordinates
from components.death_listeners.drop_gold import DropGold
from components.diggable import Diggable
from components.material import Material
from components.states.move_cost_affectors import DifficultTerrain
from components.pathfinder_cost import PathfinderCost
from engine import core, palettes
from engine.components.component import Component
from engine.components.entity import Entity
from engine.constants import PRIORITY_LOWEST


def make_rock(x, y):
    entity_id = core.get_id()
    appearance = random.choice(["%", "\"", "'", "."])
    entity: Tuple[int, List[Component]] = (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='rock', static=True),
            Appearance(entity=entity_id, symbol=appearance, color=palettes.STONE, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOWEST),
            Material(entity=entity_id, blocks=False, blocks_sight=False),
            DifficultTerrain(entity=entity_id),
            Diggable(entity=entity_id),
            PathfinderCost(entity=entity_id, cost=4)
        ]
    )
    if random.randint(1, 20) == 1:
        entity[1].append(DropGold(entity=entity_id))
    return entity
