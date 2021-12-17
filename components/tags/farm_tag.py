from dataclasses import dataclass

from components.tags.tag import Tag


@dataclass
class FarmTag(Tag):
    value: str = 'farm'
