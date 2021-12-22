import logging
from dataclasses import dataclass
from typing import List

from components.actors.energy_actor import EnergyActor
from components.build_world_listeners.build_world_listeners import BuildWorldListener
from engine.core import log_debug


@dataclass
class BuildWorld(EnergyActor):
    """Event to trigger world building steps."""
    energy_cost: int = EnergyActor.INSTANT

    @log_debug(__name__)
    def act(self, scene):
        logging.info("Building world...")
        start_game_actors: List[BuildWorldListener] = scene.cm.get(BuildWorldListener)
        for start_game_actor in start_game_actors:
            start_game_actor.on_build_world(scene)

        scene.cm.delete_component(self)

