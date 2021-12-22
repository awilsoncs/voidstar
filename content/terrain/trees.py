from components import Entity, Appearance, Coordinates, Attributes
from components.death_listeners.drop_log import DropFallenLog
from components.death_listeners.npc_corpse import Corpse
from components.faction import Faction
from components.material import Material
from components.tags.tree_tag import TreeTag
from engine import core, palettes
from engine.constants import PRIORITY_MEDIUM


def make_wall_tree(x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='tree', static=True, zone=0),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_MEDIUM, terrain=True),
            Appearance(entity=entity_id, symbol='♣', color=palettes.FOILAGE_B, bg_color=palettes.BACKGROUND),
            Material(entity=entity_id, blocks=True, blocks_sight=True)
        ]
    )


def make_tree(x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='tree', static=True, zone=0),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_MEDIUM, terrain=True),
            Attributes(entity=entity_id, hp=5, max_hp=5),
            Corpse(entity=entity_id, symbol="%", color=palettes.WOOD),
            DropFallenLog(entity=entity_id),
            Faction(entity=entity_id, faction=Faction.Options.NEUTRAL),
            Appearance(entity=entity_id, symbol='♣', color=palettes.FOILAGE_C, bg_color=palettes.BACKGROUND),
            Material(entity=entity_id, blocks=True, blocks_sight=True),
            TreeTag(entity=entity_id)
        ]
    )
