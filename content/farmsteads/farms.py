from components import Coordinates, Appearance
from components.relationships.farmed_by import FarmedBy
from components.attack_start_listeners.grow_crops import GrowCrops
from engine import core, palettes
from engine.components.entity import Entity
from engine.constants import PRIORITY_LOW

description = "A field, turned for planting. By the end of Spring and Summer, the peasant will grow crops here."


def make_farm_plot(x, y, farmer, crop_color=palettes.FIRE):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='farm_plot', description=description),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOW),
            Appearance(entity=entity_id, symbol='≈', color=palettes.DIRT, bg_color=palettes.BACKGROUND),
            FarmedBy(entity=entity_id, farmer=farmer),
            GrowCrops(entity=entity_id, crop_color=crop_color)
        ]
    )
