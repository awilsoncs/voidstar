from dataclasses import dataclass

from engine import constants
from engine.components.component import Component


@dataclass
class FarmedBy(Component):
    farmer: str = constants.INVALID
