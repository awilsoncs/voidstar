from dataclasses import dataclass

from engine.component import Component


@dataclass
class Tag(Component):
    value: str = ''
