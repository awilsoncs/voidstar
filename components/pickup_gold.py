from dataclasses import dataclass

from components.base_components.component import Component


@dataclass
class GoldPickup(Component):
    amount: int = 10
