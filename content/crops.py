from components import Entity, Coordinates, Appearance
from components.relationships.farmed_by import FarmedBy
from components.season_reset_listeners.die_in_winter import DieInWinter
from components.tags.crop_info import CropInfo
from components.tax_value import TaxValue
from engine import core, palettes
from engine.constants import PRIORITY_LOW


def make_crops(x, y, farmer, field_id):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='crop'),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOW),
            Appearance(entity=entity_id, symbol='δ', color=palettes.FIRE, bg_color=palettes.BACKGROUND),
            FarmedBy(entity=entity_id, farmer=farmer),
            CropInfo(entity=entity_id, field_id=field_id, farmer_id=farmer),
            TaxValue(entity=entity_id, value=TaxValue.CROPS),
            DieInWinter(entity=entity_id)
        ]
    )
