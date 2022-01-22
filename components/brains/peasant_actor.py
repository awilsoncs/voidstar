import random
from dataclasses import dataclass
from enum import Enum

from components.actors import STEPS
from components.base_components.energy_actor import EnergyActor
from components.brains.brain import Brain
from engine.core import log_debug


@dataclass
class PeasantActor(Brain):
    class State(str, Enum):
        UNKNOWN = 'UNKNOWN'
        FARMING = 'FARMING'
        HIDING = 'HIDING'
        WANDERING = 'WANDERING'

    state: State = State.UNKNOWN
    can_animate: bool = True
    energy_cost: int = EnergyActor.HOURLY

    @log_debug(__name__)
    def act(self, scene):
        if self.state is PeasantActor.State.FARMING:
            self.farm(scene)
        elif self.state is PeasantActor.State.WANDERING:
            self.wander(scene)
        else:
            self.pass_turn()

    def farm(self, scene):
        self.pass_turn()

    def wander(self, scene):
        self.intention = random.choice(STEPS)
