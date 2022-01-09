from typing import List

from components import Entity, Coordinates, Appearance, target_value, Attributes
from components.edible import Edible
from components.faction import Faction
from components.target_value import TargetValue
from components.tax_value import TaxValue
from engine import core, palettes
from engine.component import Component
from engine.constants import PRIORITY_MEDIUM

cows_description = "A cow, happily feasting on grass."


def make_cow(x, y) -> Entity:
    entity_id = core.get_id()
    components: List[Component] = [
        Entity(
            id=entity_id,
            entity=entity_id,
            name='cows',
            description=cows_description
        ),
        Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_MEDIUM),
        Appearance(entity=entity_id, symbol='C', color=palettes.WHITE, bg_color=palettes.BACKGROUND),
        TaxValue(entity=entity_id, value=TaxValue.COW),
        TargetValue(entity=entity_id, value=target_value.COW),
        Faction(entity=entity_id, faction=Faction.Options.PEASANT),
        Edible(entity=entity_id, sleep_for=7),
        Attributes(entity=entity_id, hp=5, max_hp=5),
    ]
    return entity_id, components
