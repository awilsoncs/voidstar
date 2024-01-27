from dataclasses import dataclass

from engine import constants
from engine.components.component import Component


@dataclass
class CropInfo(Component):
    field_id: int = constants.INVALID
    farmer_id: int = constants.INVALID
