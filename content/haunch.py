from typing import List

from components import Entity, Coordinates, Appearance, target_value, Attributes
from components.death_listeners.npc_corpse import Corpse
from components.faction import Faction
from components.relationships.farmed_by import FarmedBy
from components.season_reset_listeners.die_in_winter import DieInWinter
from components.season_reset_listeners.die_on_season_reset import DieOnSeasonReset
from components.tags.crop_info import CropInfo
from components.target_value import TargetValue
from components.tax_value import TaxValue
from engine import core, palettes
from engine.component import Component
from engine.constants import PRIORITY_LOW

haunch_description = "A savory haunch. Hordelings find this highly desirable."


def make_haunch(x, y) -> Entity:
    entity_id = core.get_id()
    components: List[Component] = [
        Entity(
            id=entity_id,
            entity=entity_id,
            name='haunch',
            description=haunch_description
        ),
        Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOW),
        Appearance(entity=entity_id, symbol='α', color=palettes.MEAT, bg_color=palettes.BACKGROUND),
        TargetValue(entity=entity_id, value=target_value.HAUNCH),
        Faction(entity=entity_id, faction=Faction.Options.PEASANT),
        Attributes(entity=entity_id, hp=1, max_hp=1),
        DieOnSeasonReset(entity=entity_id)
    ]
    return entity_id, components
