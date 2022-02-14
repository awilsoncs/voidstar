from collections import Callable
from dataclasses import dataclass

from components.abilities.control_mode_ability import ControlModeAbility
from components.brains.ability_actors.place_bomb_actor import PlaceBombActor
from engine import palettes


@dataclass
class PlaceBombAbility(ControlModeAbility):
    ability_title: str = "Place Bomb"
    unlock_cost: int = 100
    use_cost: int = 10

    def get_mode(self) -> Callable:
        return PlaceBombActor

    def get_anim(self):
        return 'δ', palettes.STONE
