from dataclasses import dataclass, field

from components.component import component_repr
from engine.core import get_id


@dataclass
class Entity:
    entity: int
    name: str
    zone: int
    abstract: bool = False
    static: bool = False  # if true, hide from 'interact' functionality
    id: int = field(default_factory=get_id)

    def get_readable_key(self):
        return f'{self.name}@{self.id}'

    def __repr__(self):
        return component_repr(self)
