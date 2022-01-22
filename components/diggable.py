from dataclasses import dataclass

from components.base_components.component import Component


@dataclass
class Diggable(Component):
    is_free: bool = False
    pass
