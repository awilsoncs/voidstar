from dataclasses import dataclass

from components.tags.tag import Tag
from engine import constants


@dataclass
class Resident(Tag):
    resident: int = constants.INVALID
    value: str = 'house'
