from dataclasses import dataclass

from engine.components.component import Component


@dataclass
class Tag(Component):
    value: str = ''
