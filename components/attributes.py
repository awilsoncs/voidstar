from dataclasses import dataclass

from engine.components.component import Component


@dataclass
class Attributes(Component):
    hp: int = 10
    max_hp: int = 10
