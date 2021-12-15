from typing import Tuple, List

from components import Entity, Appearance, Coordinates
from components.season_reset_listeners.rebuilder import Rebuilder
from components.tags.house_tag import HouseTag
from engine import palettes
from engine.component import Component
from engine.constants import PRIORITY_MEDIUM


def make_floorboard(root_id, x, y) -> Tuple[int, List[Component]]:
    return (
        root_id,
        [
            Entity(id=root_id, entity=root_id, name='floorboard'),
            Appearance(entity=root_id, symbol='=', color=palettes.STRAW, bg_color=palettes.BACKGROUND),
            Coordinates(entity=root_id, x=x, y=y, priority=PRIORITY_MEDIUM),
            Rebuilder(entity=root_id),
            HouseTag(entity=root_id)
        ]
    )