from dataclasses import dataclass, field

from engine.core import get_id


@dataclass
class Component(object):
    id: int = field(default_factory=get_id)
    entity: int = None