from dataclasses import dataclass

from engine.base_components.component import Component


@dataclass
class Tag(Component):
    value: str = ''
