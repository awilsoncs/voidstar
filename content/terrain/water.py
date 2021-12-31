from components import Entity, Appearance, Coordinates
from components.diggable import Diggable
from components.flooder import Flooder
from components.material import Material
from components.pathfinder_cost import PathfinderCost
from engine import core, palettes
from engine.constants import PRIORITY_LOWEST


def make_water(x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='water', static=True),
            Appearance(entity=entity_id, symbol='~', color=palettes.LIGHT_WATER, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOWEST),
            Material(entity=entity_id, blocks=True, blocks_sight=False),
            Diggable(entity=entity_id),
            Flooder(entity=entity_id),
            PathfinderCost(entity=entity_id, cost=0)
        ]
    )
