from dataclasses import dataclass

from components.base_components.component import Component


@dataclass
class Edible(Component):
    sleep_for: int = 3
