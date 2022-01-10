from dataclasses import dataclass, field
from typing import List

from components.tags.tag import Tag


@dataclass
class IceTag(Tag):
    value: str = 'ice'
    frozen_components: List[int] = field(default_factory=list)
