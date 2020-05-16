from components import Entity, Appearance, Brain, Attributes
from components.attack import Attack
from components.enums import ControlMode
from components.faction import Faction
from components.material import Material
from components.tags import Tag
from engine import core, palettes


def make_hordeling(zone_id):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='hordeling', zone=zone_id),
            Faction(entity=entity_id, faction=Faction.Options.MONSTER),
            Brain(entity=entity_id, control_mode=ControlMode.MONSTER),
            Appearance(entity=entity_id, symbol='h', color=palettes.HORDELING, bg_color=palettes.BACKGROUND),
            Attributes(entity=entity_id, hp=1, max_hp=1),
            Attack(entity=entity_id, damage='1d1'),
            Material(entity=entity_id, blocks=True, blocks_sight=False),
            Tag(entity=entity_id, value='hordeling')
        ]
    )
