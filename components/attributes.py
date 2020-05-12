from dataclasses import field, dataclass

from components.component import component_repr
from engine.core import get_id


@dataclass
class Attributes:
    entity: int
    hp: int = 10
    max_hp: int = 10
    id: int = field(default_factory=get_id)

    def __repr__(self):
        return component_repr(self)
