import random
from dataclasses import dataclass

from components import Brain
from components.brains import STEPS
from engine.core import log_debug
from systems.utilities import set_intention


@dataclass
class PeasantBrain(Brain):

    @log_debug(__name__)
    def act(self, scene):
        set_intention(scene, self.entity, 0, random.choice(STEPS))
