from typing import List

from components import Coordinates, Appearance, target_value, Attributes
from components.faction import Faction
from components.season_reset_listeners.die_on_season_reset import DieOnSeasonReset
from components.target_value import TargetValue
from engine import core, palettes
from engine.base_components.component import Component
from engine.base_components.entity import Entity
from engine.constants import PRIORITY_LOW

haunch_description = "A savory haunch. Hordelings find this highly desirable."


def make_haunch(x, y):
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
