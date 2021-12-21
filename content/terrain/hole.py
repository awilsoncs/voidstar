from components import Entity, Appearance, Coordinates
from components.diggable import Diggable
from components.floodable import Floodable
from components.hole_dug_listeners.hole_dug_event import HoleDugEvent
from components.material import Material
from components.states.swamped_state import DifficultTerrain
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
            Material(entity=entity_id, blocks=False, blocks_sight=False),
            Diggable(entity=entity_id),
            Floodable(entity=entity_id),
            DifficultTerrain(entity=entity_id),
            HoleDugEvent(entity=entity_id)
        ]
    )
