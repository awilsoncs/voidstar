from components import Entity, Coordinates, Appearance, Attributes
from components.Sellable import Sellable
from components.death_listeners.npc_corpse import Corpse
from components.faction import Faction
from components.material import Material
from components.season_reset_listeners.grow_in_spring import GrowInSpring
from components.pathfinder_cost import PathfinderCost
from engine import core, palettes
from engine.constants import PRIORITY_MEDIUM


def make_sapling(x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='tree', static=True),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_MEDIUM),
            Attributes(entity=entity_id, hp=2, max_hp=2),
            Corpse(entity=entity_id, symbol="%", color=palettes.FOILAGE_C),
            Faction(entity=entity_id, faction=Faction.Options.NEUTRAL),
            Appearance(entity=entity_id, symbol='+', color=palettes.FOILAGE_C, bg_color=palettes.BACKGROUND),
            Material(entity=entity_id, blocks=True, blocks_sight=False),
            GrowInSpring(entity=entity_id),
            PathfinderCost(entity=entity_id, cost=10),
            Sellable(entity=entity_id, value=0),
        ]
    )
