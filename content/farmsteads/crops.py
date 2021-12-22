from components import Entity, Coordinates, Appearance, target_value, Attributes
from components.death_listeners.npc_corpse import Corpse
from components.faction import Faction
from components.relationships.farmed_by import FarmedBy
from components.season_reset_listeners.die_in_winter import DieInWinter
from components.tags.crop_info import CropInfo
from components.target_value import TargetValue
from components.tax_value import TaxValue
from engine import core, palettes
from engine.constants import PRIORITY_LOW

crops_description = "A valuable crop. Easy pickings for the hordelings, " \
                    "but will sell for 5 gold at the end of the season- if you protect them."

def make_crops(x, y, farmer, field_id):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(
                id=entity_id,
                entity=entity_id,
                name='crop',
                description=crops_description
            ),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOW),
            Appearance(entity=entity_id, symbol='δ', color=palettes.FIRE, bg_color=palettes.BACKGROUND),
            FarmedBy(entity=entity_id, farmer=farmer),
            CropInfo(entity=entity_id, field_id=field_id, farmer_id=farmer),
            TaxValue(entity=entity_id, value=TaxValue.CROPS),
            DieInWinter(entity=entity_id),
            TargetValue(entity=entity_id, value=target_value.CROPS),
            Faction(entity=entity_id, faction=Faction.Options.PEASANT),
            Attributes(entity=entity_id, hp=1, max_hp=1),
            Corpse(entity=entity_id, color=palettes.FIRE)
        ]
    )
