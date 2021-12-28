from dataclasses import dataclass

from engine.component import Component


@dataclass
class TaxValue(Component):
    DEFAULT = 1
    CROPS = 5
    COW = 25

    value: int = DEFAULT
