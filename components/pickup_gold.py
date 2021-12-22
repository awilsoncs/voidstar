from dataclasses import dataclass

from engine.component import Component


@dataclass
class PickupGold(Component):
    amount: int = 10
