from typing import List, Tuple

from components import Entity, Appearance, Attributes, Coordinates
from components.corpse import Corpse
from components.faction import Faction
from components.house_structure import HouseStructure
from components.material import Material
from components.owner import Owner
from components.tags.house_tag import HouseTag
from content.allies import make_peasant
from engine import core, palettes
from engine.component import Component
from engine.constants import PRIORITY_MEDIUM


def make_wall(house_id, x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='wall'),
            Owner(entity=entity_id, owner=house_id),
            Appearance(entity=entity_id, symbol='#', color=palettes.STRAW, bg_color=palettes.BACKGROUND),
            Corpse(entity=entity_id, symbol='%', color=palettes.STRAW, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_MEDIUM),
            Attributes(entity=entity_id, hp=80, max_hp=80),
            Faction(entity=entity_id, faction=Faction.Options.PEASANT),
            Material(entity=entity_id, blocks=True, blocks_sight=False),
        ]
    )


def make_floorboard(house_id, x, y) -> Tuple[int, List[Component]]:
    entity_id = core.get_id()

    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='wall'),
            Owner(entity=entity_id, owner=house_id),
            Appearance(entity=entity_id, symbol='=', color=palettes.STRAW, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_MEDIUM),
            HouseTag(entity=entity_id)
        ]
    )


def make_house(house_id, x, y):
    floorboard = make_floorboard(house_id, x, y)

    upper_left = make_wall(house_id, x-1, y-1)
    upper_middle = make_wall(house_id, x, y-1)
    upper_right = make_wall(house_id, x+1, y-1)
    middle_left = make_wall(house_id, x-1, y)
    middle_right = make_wall(house_id, x+1, y)
    bottom_left = make_wall(house_id, x-1, y+1)
    bottom_middle = make_wall(house_id, x, y+1)
    bottom_right = make_wall(house_id, x+1, y+1)

    structure = HouseStructure(
        entity=floorboard[0],
        house_id=house_id,
        upper_left=upper_left[0],
        upper_middle=upper_middle[0],
        upper_right=upper_right[0],
        middle_left=middle_left[0],
        middle_right=middle_right[0],
        bottom_left=bottom_left[0],
        bottom_middle=bottom_middle[0],
        bottom_right=bottom_right[0]
    )

    floorboard[1].append(structure)

    return [
        upper_left, upper_middle, upper_right,
        middle_left, floorboard, middle_right,
        bottom_left, bottom_middle, bottom_right
    ]


def make_peasant_home(x, y):
    house_id = core.get_id()
    peasant = make_peasant(house_id, x, y)
    return make_house(house_id, x, y) + [peasant]
