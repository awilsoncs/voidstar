from typing import List

from components import Coordinates, Appearance, target_value, Attributes
from components.death_listeners.npc_corpse import Corpse
from components.edible import Edible
from components.faction import Faction
from components.relationships.farmed_by import FarmedBy
from components.tags.crop_info import CropInfo
from components.target_value import TargetValue
from components.tax_value import TaxValue
from engine import core, palettes
from engine.components.component import Component
from engine.components.entity import Entity
from engine.constants import PRIORITY_LOW

crops_description = "A valuable crop. They're easy pickens for the hordelings, " \
                    "but they will sell for 5 gold at the end of the season- if you protect them."


def make_crops(x, y, farmer, field_id, color=palettes.FIRE) -> Entity:
    entity_id = core.get_id()
    components: List[Component] = [
        Entity(
            id=entity_id,
            entity=entity_id,
            name='crop',
            description=crops_description
        ),
        Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOW),
        Appearance(entity=entity_id, symbol='δ', color=color, bg_color=palettes.BACKGROUND),
        FarmedBy(entity=entity_id, farmer=farmer),
        CropInfo(entity=entity_id, field_id=field_id, farmer_id=farmer),
        TaxValue(entity=entity_id, value=TaxValue.CROPS),
        TargetValue(entity=entity_id, value=target_value.CROPS),
        Faction(entity=entity_id, faction=Faction.Options.PEASANT),
        Attributes(entity=entity_id, hp=3, max_hp=3),
        Edible(entity=entity_id, sleep_for=10),
        Corpse(entity=entity_id, color=color)
    ]
    return entity_id, components
