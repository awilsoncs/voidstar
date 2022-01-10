from dataclasses import dataclass

from engine.component import Component


@dataclass
class Structure(Component):
    """Mark that an entity is a structure."""
    pass
