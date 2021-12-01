from dataclasses import dataclass

from components.tags.tag import Tag


@dataclass
class PeasantTag(Tag):
    value: str = 'peasant'
