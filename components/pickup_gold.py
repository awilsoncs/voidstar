from dataclasses import dataclass

from engine.base_components.component import Component


@dataclass
class GoldPickup(Component):
    amount: int = 10
