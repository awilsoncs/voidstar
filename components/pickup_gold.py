from dataclasses import dataclass

from engine.component import Component


@dataclass
class GoldPickup(Component):
    amount: int = 10
