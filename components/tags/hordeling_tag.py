from dataclasses import dataclass

from components.tags.tag import Tag
from engine.component import Component


@dataclass
class HordelingTag(Tag):
    value: str = 'hordeling'
