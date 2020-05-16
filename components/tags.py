from dataclasses import dataclass

from components.component import Component


@dataclass
class Tag(Component):
    value: str = ''
