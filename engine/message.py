from dataclasses import dataclass
from typing import Tuple

from engine import palettes


@dataclass
class Message:
    text: str = ''
    color: Tuple[int, int, int] = palettes.MEAT
