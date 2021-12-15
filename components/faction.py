import enum
from dataclasses import dataclass

from engine.component import Component


@dataclass
class Faction(Component):

    class Options(enum.Enum):
        NONE = 'none'
        MONSTER = 'monster'
        PEASANT = 'peasant'
        NEUTRAL = 'neutral'

    faction: Options = Options.NONE
