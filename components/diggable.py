from dataclasses import dataclass

from engine.components.component import Component


@dataclass
class Diggable(Component):
    is_free: bool = False
    pass
