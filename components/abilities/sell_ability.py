from dataclasses import dataclass
from typing import Callable

from components.abilities.control_mode_ability import ControlModeAbility
from components.brains.ability_actors.sell_thing_actor import SellThingActor
from engine import palettes


@dataclass
class SellAbility(ControlModeAbility):
    ability_title: str = "Sell Things"
    unlock_cost: int = 0
    use_cost: int = 0

    def get_mode(self) -> Callable:
        return SellThingActor

    def get_anim(self):
        return '$', palettes.GOLD
