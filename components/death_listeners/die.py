import logging
from dataclasses import dataclass
from typing import List, Optional, Tuple

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
        death_listeners: List[DeathListener] = scene.cm.get_all(DeathListener, entity=self.entity)
        for death_listener in death_listeners:
            death_listener.on_die(scene)
        scene.cm.delete(self.entity)
