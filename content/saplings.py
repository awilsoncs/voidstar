from components import Entity, Coordinates, Appearance, Attributes
from components.corpse import Corpse
from components.faction import Faction
from components.material import Material
from components.season_reset_listeners.grow_in_spring import GrowInSpring
from engine import core, palettes
from engine.constants import PRIORITY_MEDIUM


def make_sapling(x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='tree', static=True, zone=0),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_MEDIUM, terrain=True),
            Attributes(entity=entity_id, hp=2, max_hp=2),
            Corpse(entity=entity_id, symbol="%", color=palettes.FOILAGE_C),
            Faction(entity=entity_id, faction=Faction.Options.MONSTER),
            Appearance(entity=entity_id, symbol='+', color=palettes.FOILAGE_C, bg_color=palettes.BACKGROUND),
            Material(entity=entity_id, blocks=True, blocks_sight=True),
            GrowInSpring(entity=entity_id)
        ]
    )
