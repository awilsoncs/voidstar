from dataclasses import dataclass

from engine.component import Component


@dataclass
class Hindered(Component):
    factor: float = 2.0


@dataclass
class Hindrance(Component):
    factor: float = 2.0
