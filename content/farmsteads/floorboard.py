from typing import Tuple, List

from components import Appearance, Coordinates
from components.season_reset_listeners.rebuilder import Rebuilder
from components.relationships.resident import Resident
from engine import palettes
from components.base_components.component import Component
from components.base_components.entity import Entity
from engine.constants import PRIORITY_MEDIUM

description = "Kinda creepy to be looking in this person's house, no?"


def make_floorboard(root_id, x, y, resident) -> Tuple[int, List[Component]]:
    return (
        root_id,
        [
            Entity(id=root_id, entity=root_id, name='floorboard', description=description),
            Appearance(entity=root_id, symbol='=', color=palettes.STRAW, bg_color=palettes.BACKGROUND),
            Coordinates(entity=root_id, x=x, y=y, priority=PRIORITY_MEDIUM),
            Rebuilder(entity=root_id),
            Resident(entity=root_id, resident=resident)
        ]
    )
