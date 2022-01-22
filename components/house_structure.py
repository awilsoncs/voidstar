from dataclasses import dataclass
from typing import List

from components.base_components.component import Component
from engine.types import EntityId


@dataclass
class HouseStructure(Component):
    house_id: EntityId = 0
    upgrade_level: int = 0
    is_destroyed: bool = False
    upper_left: EntityId = 0
    upper_middle: EntityId = 0
    upper_right: EntityId = 0
    middle_left: EntityId = 0
    middle_right: EntityId = 0
    bottom_left: EntityId = 0
    bottom_middle: EntityId = 0
    bottom_right: EntityId = 0

    def get_all(self) -> List[EntityId]:
        return [
            self.upper_left, self.upper_middle, self.upper_right,
            self.middle_left, self.middle_right,
            self.bottom_left, self.bottom_middle, self.bottom_right
        ]
