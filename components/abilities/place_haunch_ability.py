from collections import Callable
from dataclasses import dataclass

from components.abilities.control_mode_ability import ControlModeAbility
from components.brains.hire_knight_brain import HireKnightActor
from components.brains.place_haunch_actor import PlaceHaunchActor
from components.enums import Intention
from engine import palettes


@dataclass
class PlaceHaunchAbility(ControlModeAbility):
    ability_title: str = "Place Haunch"
    unlock_cost: int = 100
    use_cost: int = 15
    intention: Intention = Intention.PLACE_HAUNCH

    def get_mode(self) -> Callable:
        return PlaceHaunchActor

    def get_anim(self):
        return 'α', palettes.MEAT
