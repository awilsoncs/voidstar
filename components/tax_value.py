from dataclasses import dataclass

from engine.components.component import Component


@dataclass
class TaxValue(Component):
    DEFAULT = 1
    CROPS = 1
    COW = 25
    KNIGHT = -15

    value: int = DEFAULT
    fund: int = "General Fund"
