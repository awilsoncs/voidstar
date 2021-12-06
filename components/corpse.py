from dataclasses import dataclass

from engine import palettes
from engine.component import Component


@dataclass
class Corpse(Component):
    symbol: str = '%'
    color: tuple = palettes.BLOOD
    bg_color: tuple = palettes.BACKGROUND
