from dataclasses import dataclass

from engine.component import Component


@dataclass
class TownCenterFlag(Component):
    """Mark the town center."""
    pass
