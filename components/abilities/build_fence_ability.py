from collections import Callable
from dataclasses import dataclass

from components.abilities.control_mode_ability import ControlModeAbility
from components.enums import Intention
from components.brains.place_fence_actor import PlaceFenceActor
from engine import palettes


@dataclass
class BuildFenceAbility(ControlModeAbility):
    ability_title: str = "Build Fence"
    unlock_cost: int = 100
    use_cost: int = 5
    intention: Intention = Intention.BUILD_FENCE

    def get_mode(self) -> Callable:
        return PlaceFenceActor

    def get_anim(self):
        return 'o', palettes.WOOD
