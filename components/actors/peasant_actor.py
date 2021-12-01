import random
from dataclasses import dataclass

from components.actors import STEPS
from components.actors.energy_actor import EnergyActor
from engine.core import log_debug
from systems.utilities import set_intention


@dataclass
class PeasantTimedActor(EnergyActor):

    @log_debug(__name__)
    def act(self, scene):
        set_intention(scene, self.entity, 0, random.choice(STEPS))
