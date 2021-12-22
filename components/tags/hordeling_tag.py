from dataclasses import dataclass

from components.tags.tag import Tag


@dataclass
class HordelingTag(Tag):
    value: str = 'hordeling'
