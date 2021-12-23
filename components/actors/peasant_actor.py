import logging
import random
from dataclasses import dataclass
from enum import auto, Enum
from typing import List, Tuple

from components import Coordinates
from components.actors import STEPS
from components.actors.energy_actor import EnergyActor
from components.relationships.farmed_by import FarmedBy
from content.farmsteads.farm_animation import farm_animation
from engine.core import log_debug
from systems.utilities import set_intention


@dataclass
class PeasantActor(EnergyActor):
    class State(Enum):
        UNKNOWN = auto()
        FARMING = auto()
        HIDING = auto()
        WANDERING = auto()

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
        if not self.can_animate:
            return

        logging.debug(f"EID#{self.entity}:PeasantActor farming")
        self.can_animate = False

        farm_tiles: List[Coordinates] = scene.cm.get(
            FarmedBy,
            query=lambda fb: fb.farmer == self.entity,
            project=lambda fb: scene.cm.get_one(Coordinates, entity=fb.entity)
        )

        my_coords: Coordinates = scene.cm.get_one(Coordinates, entity=self.entity)
        farmable_tiles: List[Tuple[int, int]] = [
            (ft.x, ft.y)
            for ft in farm_tiles
            if ft.x != my_coords.x or ft.y != my_coords.y
        ]
        target_tile = random.choice(farmable_tiles)

        farm = farm_animation(self.entity, target_tile[0], target_tile[1])
        scene.cm.add(*farm[1])
        delay = random.randint(EnergyActor.HOURLY, EnergyActor.HOURLY*6)
        self.pass_turn(delay)

    def wander(self, scene):
        set_intention(scene, self.entity, 0, random.choice(STEPS))

