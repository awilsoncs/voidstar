from components import Entity, Coordinates, Appearance
from components.animation_effects.float import AnimationFloat
from components.owner import Owner
from engine import core, palettes
from engine.constants import PRIORITY_HIGH


def dizzy_animation(owner, x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='dizzy'),
            Appearance(entity=entity_id, symbol='?', color=palettes.LIGHT_WATER, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_HIGH),
            Owner(entity=entity_id, owner=owner),
            AnimationFloat(entity=entity_id, delay_ms=125, duration=10),
        ]
    )
