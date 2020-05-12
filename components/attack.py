from dataclasses import field, dataclass

from components.component import component_repr
from engine.core import get_id


@dataclass
class Attack:
    entity: int = None
    damage: str = '1d6'
    id: int = field(default_factory=get_id)

    def __repr__(self):
        return component_repr(self)
