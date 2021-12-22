from dataclasses import dataclass
from typing import List

from components.actors.energy_actor import EnergyActor
from components.game_start_listeners.game_start_listener import GameStartListener
from engine.core import log_debug


@dataclass
class StartGame(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT

    @log_debug(__name__)
    def act(self, scene):
        start_game_actors: List[GameStartListener] = scene.cm.get(GameStartListener)
        for start_game_actor in start_game_actors:
            start_game_actor.on_game_start(scene)

        scene.cm.delete_component(self)
