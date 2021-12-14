from components import Entity, Appearance, Coordinates
from components.material import Material
from engine import core, palettes
from engine.constants import PRIORITY_MEDIUM


def make_sapling(x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='tree', static=True, zone=0),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_MEDIUM, terrain=True),
            Appearance(entity=entity_id, symbol='+', color=palettes.FOILAGE_C, bg_color=palettes.BACKGROUND),
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
            Appearance(entity=entity_id, symbol='♣', color=palettes.FOILAGE_C, bg_color=palettes.BACKGROUND),
            Material(entity=entity_id, blocks=True, blocks_sight=True)
        ]
    )
