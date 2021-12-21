import random
from typing import List, Tuple

from components import Entity, Appearance, Coordinates
from components.death_listeners.drop_gold import DropGold
from components.diggable import Diggable
from components.material import Material
from components.states.swamped_state import Swamper
from engine import core, palettes
from engine.component import Component
from engine.constants import PRIORITY_LOWEST


def make_rock(x, y):
    entity_id = core.get_id()
    appearance = "\"" if random.random() < .5 else "'"
    entity: Tuple[int, List[Component]] = (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='rock', static=True),
            Appearance(entity=entity_id, symbol=appearance, color=palettes.STONE, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOWEST, terrain=True),
            Material(entity=entity_id, blocks=False, blocks_sight=False),
            Swamper(entity=entity_id),
            Diggable(entity=entity_id)
        ]
    )
    if random.randint(1, 20) == 1:
        entity[1].append(DropGold(entity=entity_id))
    return entity
