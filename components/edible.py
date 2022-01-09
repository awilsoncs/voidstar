from dataclasses import dataclass

from engine.component import Component


@dataclass
class Edible(Component):
    sleep_for: int = 3
