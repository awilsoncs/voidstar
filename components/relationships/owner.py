from dataclasses import dataclass

from engine.component import Component


@dataclass
class Owner(Component):
    owner: int = None
