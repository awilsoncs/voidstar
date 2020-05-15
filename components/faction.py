import enum
from dataclasses import dataclass

from components.component import Component


@dataclass
class Faction(Component):

    class Options(enum.Enum):
        NONE = 'none'
        MONSTER = 'monster'
        PEASANT = 'peasant'

    faction: Options = Options.NONE
