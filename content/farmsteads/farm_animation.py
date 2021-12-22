from components import Entity, Coordinates, Appearance
from components.animation_effects.reset_owner_animation import ResetOwnerAnimation
from components.delete_listeners.deleter import Deleter
from components.relationships.owner import Owner
from engine import palettes, core
from engine.constants import PRIORITY_HIGH


def farm_animation(owner, x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='farm_animation'),
            Appearance(entity=entity_id, symbol='/', color=palettes.STONE, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_HIGH),
            Owner(entity=entity_id, owner=owner),
            ResetOwnerAnimation(entity=entity_id),
            Deleter(entity=entity_id, next_update=core.time_ms() + 300)
        ]
    )
