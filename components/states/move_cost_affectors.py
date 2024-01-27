from dataclasses import dataclass

from engine.components.component import Component


@dataclass
class Hindered(Component):
    pass


@dataclass
class DifficultTerrain(Component):
    pass


@dataclass
class Haste(Component):
    pass


@dataclass
class EasyTerrain(Component):
    pass
