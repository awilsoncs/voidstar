from dataclasses import dataclass

from components.tags.tag import Tag


@dataclass
class IceTag(Tag):
    value: str = 'ice'
