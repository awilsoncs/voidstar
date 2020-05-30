from components import Entity, Appearance, Brain, Coordinates
from components.animation_path import AnimationPath
from components.owner import Owner
from components.path_node import create_path
from engine import core, palettes
from engine.constants import PRIORITY_HIGH


def swing_sword(owner, path):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='sword_attack'),
            Appearance(entity=entity_id, symbol='/', color=palettes.GREY, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=path[0][0], y=path[0][1], priority=PRIORITY_HIGH),
            Owner(entity=entity_id, owner=owner),
            AnimationPath(entity=entity_id, delay_ms=25),
            *create_path(entity_id, path)
        ]
    )


def thwack_animation(owner, x, y):
    """A circular spin attack centered on (x, y)."""
    return swing_sword(
        owner,
        [
            (x+1, y-1),
            (x, y-1),
            (x-1, y-1),
            (x-1, y),
            (x-1, y+1),
            (x, y+1),
            (x+1, y+1),
            (x+1, y)
        ]
    )
