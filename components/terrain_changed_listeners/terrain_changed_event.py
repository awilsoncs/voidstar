from dataclasses import dataclass
from typing import List

from components.actors.energy_actor import EnergyActor
from components.terrain_changed_listeners.terrain_changed_listener import TerrainChangedListener
from engine.core import log_debug


@dataclass
class TerrainChangedEvent(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT

    @log_debug(__name__)
    def act(self, scene):
        actors: List[TerrainChangedListener] = scene.cm.get(TerrainChangedListener)
        for actor in actors:
            actor.on_terrain_changed(scene)

        scene.cm.delete_component(self)
