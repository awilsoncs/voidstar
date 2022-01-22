from dataclasses import dataclass

from components.tags.tag import Tag


@dataclass
class WaterTag(Tag):
    value: str = 'water'
    is_dirty: bool = False
