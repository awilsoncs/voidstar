import random
from dataclasses import dataclass
from enum import Enum

import settings
from components import Coordinates
from components.actors import STEPS, VECTOR_STEP_MAP, STEP_VECTOR_MAP
from components.base_components.energy_actor import EnergyActor
from components.brains.brain import Brain
from components.enums import Intention
from components.pathfinding.cost_mapper import CostMapper
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
        cost_mapper = scene.cm.get_one(CostMapper, entity=self.entity)
        if not cost_mapper:
            self._log_debug("no cost mapper found")
            self.intention = random.choice(STEPS)
            return

        step_costs = self.get_possible_steps(scene)

        if step_costs:
            # shuffle to perturb the stable sort
            random.shuffle(step_costs)
            step_costs = sorted(step_costs, key=lambda x: x[1])
            self._log_debug(f"evaluated steps {step_costs}")
            self.intention = step_costs[0][0]
        else:
            # nowhere to go
            self.pass_turn()

    def get_possible_steps(self, scene):
        cost_mapper = scene.cm.get_one(CostMapper, entity=self.entity)
        cost_map = cost_mapper.get_cost_map(scene)
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        step_costs = []
        for step in STEPS:
            if step not in [Intention.NONE, Intention.DALLY]:
                new_position = (
                    STEP_VECTOR_MAP[step][0] + coords.position[0],
                    STEP_VECTOR_MAP[step][1] + coords.position[1]
                )
                if (
                        0 <= new_position[0] < settings.MAP_WIDTH
                        and 0 <= new_position[1] < settings.MAP_HEIGHT
                ):
                    step_cost = (step, cost_map[new_position[0], new_position[1]])
                    step_costs.append(step_cost)
        return step_costs
