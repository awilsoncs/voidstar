from typing import Callable
from dataclasses import dataclass

from components.abilities.control_mode_ability import ControlModeAbility
from components.brains.ability_actors.place_fence_actor import PlaceFenceActor
from components.brains.ability_actors.place_spikes_actor import PlaceSpikesActor
from engine import palettes



@dataclass
class BuildSpikesAbility(ControlModeAbility):
    ability_title: str = "Build Spike Trap"
    unlock_cost: int = 100
    use_cost: int = 5

    def get_mode(self) -> Callable:
        return PlaceSpikesActor

    def get_anim(self):
        return '╨', palettes.STONE
