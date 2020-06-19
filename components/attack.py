from dataclasses import dataclass

from engine.component import Component


@dataclass
class Attack(Component):
    damage: int = 1
