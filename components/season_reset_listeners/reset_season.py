from dataclasses import dataclass
from typing import List

from components.actors.energy_actor import EnergyActor
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from engine.core import log_debug


@dataclass
class ResetSeason(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT

    @log_debug(__name__)
    def act(self, scene):
        seasonal_actors: List[SeasonResetListener] = scene.cm.get(SeasonResetListener)
        for seasonal_actor in seasonal_actors:
            seasonal_actor.on_season_reset(scene)

        scene.cm.delete_component(self)
