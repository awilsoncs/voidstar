from components import Entity, Brain, Appearance, Attributes
from components.enums import ControlMode
from components.target_value import PEASANT, TargetValue
from engine import core, colors


def make_peasant(zone_id):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='peasant', zone=zone_id),
            Brain(entity=entity_id, control_mode=ControlMode.WANDER),
            Appearance(entity=entity_id, symbol='p', color=colors.white),
            Attributes(entity=entity_id, hp=10, max_hp=10),
            TargetValue(entity=entity_id, value=PEASANT)
        ]
    )
