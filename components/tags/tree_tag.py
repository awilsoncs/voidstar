from dataclasses import dataclass

from components.tags.tag import Tag


@dataclass
class TreeTag(Tag):
    value: str = 'tree'
