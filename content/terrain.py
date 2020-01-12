import random

from components import Entity, Appearance
from engine import core, colors


def make_ground(zone_id):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='ground', static=True, zone=zone_id),
            Appearance(entity=entity_id, symbol=_get_ground_symbol(), color=colors.white)
        ]
    )


def _get_ground_symbol():
    return random.choice(["`", "'", ",", ".", "\"", " "])


def make_tree(zone_id):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='tree', static=True, zone=zone_id),
            Appearance(entity=entity_id, symbol='♣', bg_color=colors.white)
        ]
    )
