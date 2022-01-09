from dataclasses import dataclass

from engine.component import Component


@dataclass
class Sellable(Component):
    value: int = 0
