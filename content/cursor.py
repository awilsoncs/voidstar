from components import Entity, TimedActor, Appearance, Coordinates
from components.enums import ControlMode
from components.relationships.owner import Owner
from engine import core, palettes
from engine.constants import PRIORITY_HIGH


def make_cursor(zone, x, y, owner):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='cursor', zone=zone),
            Owner(entity=entity_id, owner=owner),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_HIGH),
            TimedActor(entity=entity_id, control_mode=ControlMode.CURSOR),
            Appearance(entity=entity_id, symbol='X', color=palettes.GOLD, bg_color=palettes.BACKGROUND),
        ]
    )
