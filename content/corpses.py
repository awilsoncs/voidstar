import random

from components import Entity, Appearance, Coordinates
from components.events.deleter import Deleter
from components.tags import Tag
from engine import palettes, core
from engine.constants import PRIORITY_LOW


def make_corpse(name, x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name=f'{name} corpse'),
            Appearance(entity=entity_id, symbol='%', color=palettes.BLOOD, bg_color=palettes.BACKGROUND),
            Tag(entity=entity_id, value='corpse'),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOW),
            Deleter(entity=entity_id)
        ]
    )


def make_blood_pool(x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name=f'blood pool'),
            Appearance(entity=entity_id, symbol='.', color=palettes.BLOOD, bg_color=palettes.BACKGROUND),
            Tag(entity=entity_id, value='corpse'),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOW),
            Deleter(entity=entity_id)
        ]
    )


def make_blood_splatter(count, x, y):
    pools = []
    for _ in range(5):
        pools += make_blood_pool(
            x + int(random.triangular(-count, 0, count)),
            y + int(random.triangular(-count, 0, count))
        )[1]
    return pools
