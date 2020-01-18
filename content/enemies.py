from components import Entity, Appearance, Brain, Attributes
from components.enums import ControlMode
from engine import core, colors


def make_hordeling(zone_id):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='hordeling', zone=zone_id),
            Brain(entity=entity_id, control_mode=ControlMode.MONSTER),
            Appearance(entity=entity_id, symbol='h', color=colors.red),
            Attributes(entity=entity_id, hp=10, max_hp=10),
        ]
    )
