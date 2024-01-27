from dataclasses import dataclass

from engine.components.component import Component


@dataclass
class GoldPickup(Component):
    amount: int = 10
