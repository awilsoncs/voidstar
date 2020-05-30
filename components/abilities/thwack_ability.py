from dataclasses import dataclass

from components.component import Component


@dataclass
class ThwackAbility(Component):
    count: int = 0
