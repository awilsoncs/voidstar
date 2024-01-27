from typing import Callable
from dataclasses import dataclass

from components.abilities.control_mode_ability import ControlModeAbility
from components.brains.ability_actors.plant_sapling_actor import PlaceSaplingActor
from engine import palettes


@dataclass
class PlantSaplingAbility(ControlModeAbility):
    ability_title: str = "Plant Saplings"
    unlock_cost: int = 100
    use_cost: int = 1

    def get_mode(self) -> Callable:
        return PlaceSaplingActor

    def get_anim(self):
        return '+', palettes.FOILAGE_C
