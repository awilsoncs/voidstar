from dataclasses import dataclass

from components.component import Component


@dataclass
class Owner(Component):
    owner: int = None
