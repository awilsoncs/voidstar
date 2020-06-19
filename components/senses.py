from dataclasses import dataclass

import settings
from engine.component import Component


@dataclass
class Senses(Component):
    sight_radius: int = settings.TORCH_RADIUS
    dirty: bool = True
