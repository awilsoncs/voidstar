from components import Appearance, Coordinates
from components.animation_effects.path import AnimationPath
from components.events.delete_event import Delete
from components.relationships.owner import Owner
from components.path_node import create_path
from engine import core, palettes
from engine.components.entity import Entity
from engine.constants import PRIORITY_HIGH


def roundabout(owner, x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='sword_attack'),
            Coordinates(entity=entity_id, x=x + 1, y=y - 1, priority=PRIORITY_HIGH, buildable=True),
            Owner(entity=entity_id, owner=owner),
            AnimationPath(entity=entity_id),
            *create_path(
                entity_id,
                [
                    (x + 1, y - 1),
                    (x, y - 1),
                    (x - 1, y - 1),
                    (x - 1, y),
                    (x - 1, y + 1),
                    (x, y + 1),
                    (x + 1, y + 1),
                    (x + 1, y)
                ]
            )
        ]
    )


def thwack_animation(owner, x, y):
    base = roundabout(owner, x, y)
    base[1].append(Appearance(entity=base[0], symbol='/', color=palettes.STONE, bg_color=palettes.BACKGROUND))
    return base


def thwack_dizzy_animation(owner, x, y):
    base = roundabout(owner, x, y)
    base[1].append(Appearance(entity=base[0], symbol='?', color=palettes.LIGHT_WATER, bg_color=palettes.BACKGROUND))
    return base


def stab(owner, x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='sword_attack'),
            Appearance(entity=entity_id, symbol='/', color=palettes.STONE, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_HIGH),
            Owner(entity=entity_id, owner=owner),
            Delete(entity=entity_id, next_update=core.time_ms() + 125)
        ]
    )
