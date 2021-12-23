from dataclasses import dataclass, field

from engine import constants
from engine.core import get_id


@dataclass
class Component(object):
    id: int = field(default_factory=get_id)
    entity: int = constants.INVALID

    def on_component_delete(self, cm):
        """Called by the CM when the component is deleted."""
        pass
