from components import Entity, Coordinates, Appearance
from components.relationships.farmed_by import FarmedBy
from components.season_reset_listeners.grow_crops import GrowCrops
from engine import core, palettes
from engine.constants import PRIORITY_LOW


def make_farm_plot(x, y, farmer):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='farm_plot'),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOW),
            Appearance(entity=entity_id, symbol='=', color=palettes.DIRT, bg_color=palettes.BACKGROUND),
            FarmedBy(entity=entity_id, farmer=farmer),
            GrowCrops(entity=entity_id)
        ]
    )
