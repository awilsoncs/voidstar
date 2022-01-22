from dataclasses import dataclass

from components.base_components.component import Component


@dataclass
class Tag(Component):
    value: str = ''
