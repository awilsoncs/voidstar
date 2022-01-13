import enum
from dataclasses import dataclass

from engine.components.component import Component


@dataclass
class Faction(Component):

    class Options(str, enum.Enum):
        NONE = 'none'
        MONSTER = 'monster'
        PEASANT = 'peasant'
        NEUTRAL = 'neutral'

    faction: Options = Options.NONE
