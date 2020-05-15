from dataclasses import dataclass

from components.component import Component


@dataclass
class Attack(Component):
    damage: str = '1d6'
