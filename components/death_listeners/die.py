import logging
from dataclasses import dataclass
from typing import List

from components.actors.energy_actor import EnergyActor
from components.death_listeners.death_listener import DeathListener
from engine import constants
from engine.core import log_debug


@dataclass
class Die(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT
    killer: int = constants.INVALID

    @log_debug(__name__)
    def act(self, scene):
        logging.info(f"EID#{self.entity}::Die entity killed by {self.killer}")
        start_game_actors: List[DeathListener] = scene.cm.get_all(DeathListener, entity=self.entity)
        for start_game_actor in start_game_actors:
            start_game_actor.on_die(scene)
        scene.cm.delete(self.entity)
