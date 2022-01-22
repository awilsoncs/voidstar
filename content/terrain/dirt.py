import random
from typing import List, Tuple

from components import Appearance, Coordinates
from components.diggable import Diggable
from components.material import Material
from components.season_reset_listeners.grow_grass import GrowGrass
from engine import core, palettes
from components.base_components.component import Component
from components.base_components.entity import Entity
from engine.constants import PRIORITY_LOWEST


def make_dirt(x, y):
    entity_id = core.get_id()
    appearance = "\"" if random.random() < .5 else "'"
    entity: Tuple[int, List[Component]] = (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='dirt', static=True),
            Appearance(entity=entity_id, symbol=appearance, color=palettes.DIRT, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOWEST, buildable=True),
            Material(entity=entity_id, blocks=False, blocks_sight=False),
            Diggable(entity=entity_id, is_free=True),
            GrowGrass(entity=entity_id)
        ]
    )
    return entity
