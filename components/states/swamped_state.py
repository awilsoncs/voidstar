from dataclasses import dataclass

from engine.component import Component


@dataclass
class Swamped(Component):
    pass


@dataclass
class Swamper(Component):
    pass
