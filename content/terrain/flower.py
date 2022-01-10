import random

from components import Entity, Appearance, Coordinates
from components.material import Material
from engine import palettes, core
from engine.constants import PRIORITY_LOWEST


def make_flower(x, y):
    entity_id = core.get_id()

    color = random.choice([palettes.FRESH_BLOOD, palettes.GOLD, palettes.WHITE, palettes.WATER])

    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='flower'),
            Appearance(entity=entity_id, symbol='*', color=color, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOWEST),
            Material(entity=entity_id, blocks=False, blocks_sight=False)
        ]
    )
