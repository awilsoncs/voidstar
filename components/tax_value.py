from dataclasses import dataclass

from engine.base_components.component import Component


@dataclass
class TaxValue(Component):
    DEFAULT = 1
    CROPS = 1
    COW = 25

    value: int = DEFAULT
