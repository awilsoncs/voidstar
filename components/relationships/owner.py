from dataclasses import dataclass

from engine.base_components.component import Component


@dataclass
class Owner(Component):
    owner: int = None
