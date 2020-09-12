from components import Entity, Appearance, Coordinates
from components.material import Material
from components.states.swamped_state import Swamper
from engine import core, palettes
from engine.constants import PRIORITY_LOWEST


def make_tree(zone_id):
    entity_id = core.get_id()
    tree_color = palettes.FOILAGE_C
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='tree', static=True, zone=zone_id),
            Appearance(entity=entity_id, symbol='♣', color=tree_color, bg_color=palettes.BACKGROUND),
            Material(entity=entity_id, blocks=True, blocks_sight=True)
        ]
    )


def make_water(x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='tree', static=True),
            Appearance(entity=entity_id, symbol='~', color=palettes.LIGHT_WATER, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOWEST, terrain=True),
            Material(entity=entity_id, blocks=False, blocks_sight=False),
            Swamper(entity=entity_id)
        ]
    )
