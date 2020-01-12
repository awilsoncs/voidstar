from components import Entity, Brain, Appearance, Coordinates
from components.enums import ControlMode
from components.owner import Owner
from engine import core, colors
from engine.constants import PRIORITY_HIGH


def make_cursor(zone, x, y, owner):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='cursor', zone=zone),
            Owner(entity=entity_id, owner=owner),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_HIGH),
            Brain(entity=entity_id, control_mode=ControlMode.CURSOR),
            Appearance(entity=entity_id, symbol='X', color=colors.yellow)
        ]
    )
