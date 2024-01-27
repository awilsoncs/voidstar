from dataclasses import dataclass

from components.abilities.control_mode_ability import ControlModeAbility
from components.brains.ability_actors.place_fence_actor import PlaceFenceActor
from engine import palettes


@dataclass
class BuildFenceAbility(ControlModeAbility):
    ability_title: str = "Build Fence"
    unlock_cost: int = 100
    use_cost: int = 5

    def get_mode(self):
        return PlaceFenceActor

    def get_anim(self):
        return 'o', palettes.WOOD
