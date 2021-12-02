from dataclasses import dataclass

from components.actors.energy_actor import EnergyActor
from components.actors.seasonal_actor import SeasonalActor
from engine.core import log_debug


@dataclass
class ResetSeason(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT

    @log_debug(__name__)
    def act(self, scene):
        seasonal_actors = scene.cm.get(SeasonalActor)
        for seasonal_actor in seasonal_actors:
            seasonal_actor.act(scene)

        scene.cm.delete_component(self)
