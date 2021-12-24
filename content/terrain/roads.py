from typing import Tuple, List

from components import Entity, Appearance, Coordinates
from engine import core, palettes
from engine.component import Component
from engine.constants import PRIORITY_LOWEST


def make_road(x, y):
    entity_id = core.get_id()
    entity: Tuple[int, List[Component]] = (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='road', static=True),
            Appearance(entity=entity_id, symbol='.', color=palettes.GOLD, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOWEST),
        ]
    )
    return entity
