from dataclasses import dataclass

from engine.base_components.component import Component


@dataclass
class Structure(Component):
    """Mark that an entity is a structure."""
    pass
