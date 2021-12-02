from dataclasses import dataclass
from typing import List

from components import Attributes
from components.actors.seasonal_actor import SeasonalActor


@dataclass
class ResetHealth(SeasonalActor):
    def act(self, scene):
        scene.popup_message("You rest and your wounds heal.")
        healths: List[Attributes] = scene.cm.get(Attributes)
        for health in healths:
            health.hp = health.max_hp
