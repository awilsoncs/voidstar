from components import Entity, Appearance, Coordinates
from engine import palettes, core
from engine.constants import PRIORITY_LOW


def make_corpse(name, x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name=f'{name} corpse'),
            Appearance(entity=entity_id, symbol='%', color=palettes.BLOOD, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOW)
        ]
    )
