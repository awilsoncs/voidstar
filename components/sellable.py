from dataclasses import dataclass

from engine.base_components.component import Component


@dataclass
class Sellable(Component):
    value: int = 0
