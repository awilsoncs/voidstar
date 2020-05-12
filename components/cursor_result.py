from dataclasses import dataclass, field

from components.component import component_repr
from engine.core import get_id


@dataclass
class CursorResult:
    id: int = field(default_factory=get_id)
    entity: int = None
    x: int = None
    y: int = None

    def __repr__(self):
        return component_repr(self)
