from components import Entity, Appearance, Coordinates
from components.material import Material
from engine import core, palettes
from engine.constants import PRIORITY_LOWEST


def make_hole(x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='hole'),
            Appearance(entity=entity_id, symbol='O', color=palettes.DIRT, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOWEST, terrain=True),
            Material(entity=entity_id, blocks=True, blocks_sight=False)
        ]
    )
