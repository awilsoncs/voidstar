import random

from components import Entity, Appearance, Coordinates
from components.events.deleter import Deleter
from components.tags.corpse_tag import CorpseTag
from engine import palettes, core
from engine.constants import PRIORITY_LOW


def make_corpse(name, x, y, symbol='%', color=palettes.BLOOD, bg_color=palettes.BACKGROUND):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name=name),
            Appearance(entity=entity_id, symbol=symbol, color=color, bg_color=bg_color),
            CorpseTag(entity=entity_id),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOW),
            Deleter(entity=entity_id)
        ]
    )


def make_blood_pool(x, y, color):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name=f'blood pool'),
            Appearance(entity=entity_id, symbol='.', color=color, bg_color=palettes.BACKGROUND),
            CorpseTag(entity=entity_id),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOW),
            Deleter(entity=entity_id)
        ]
    )


def make_blood_splatter(count, x, y, color):
    pools = []
    for _ in range(5):
        pools += make_blood_pool(
            x + int(random.triangular(-count, 0, count)),
            y + int(random.triangular(-count, 0, count)),
            color
        )[1]
    return pools
