from dataclasses import dataclass

from components.tags.tag import Tag


@dataclass
class HouseTag(Tag):
    value: str = 'house'
