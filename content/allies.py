from components import Entity, Brain, Appearance, Attributes
from components.enums import ControlMode
from components.faction import Faction
from components.material import Material
from components.target_value import PEASANT, TargetValue
from engine import core, colors


def make_peasant(zone_id):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='peasant', zone=zone_id),
            Faction(entity=entity_id, faction=Faction.Options.PEASANT),
            Brain(entity=entity_id, control_mode=ControlMode.WANDER),
            Appearance(entity=entity_id, symbol='p', color=colors.white),
            Attributes(entity=entity_id, hp=200, max_hp=200),
            TargetValue(entity=entity_id, value=PEASANT),
            Material(entity=entity_id, blocks=True, blocks_sight=False)
        ]
    )
