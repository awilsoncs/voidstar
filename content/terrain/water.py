from components import Entity, Appearance, Coordinates
from components.diggable import Diggable
from components.flooder import Flooder
from components.material import Material
from components.states.swamped_state import Swamper
from engine import core, palettes
from engine.constants import PRIORITY_LOWEST


def make_water(x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='tree', static=True),
            Appearance(entity=entity_id, symbol='~', color=palettes.LIGHT_WATER, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOWEST, terrain=True),
            Material(entity=entity_id, blocks=False, blocks_sight=False),
            Swamper(entity=entity_id),
            Diggable(entity=entity_id),
            Flooder(entity=entity_id)
        ]
    )
