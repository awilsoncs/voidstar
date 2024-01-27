from dataclasses import dataclass

from engine.components.component import Component


@dataclass
class Sellable(Component):
    value: int = 0
