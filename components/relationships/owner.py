from dataclasses import dataclass

from engine.components.component import Component


@dataclass
class Owner(Component):
    owner: int = None
