from dataclasses import dataclass

from engine.component import Component


@dataclass
class TaxValue(Component):
    DEFAULT = 1
    PEASANT = 1

    value: int = DEFAULT
