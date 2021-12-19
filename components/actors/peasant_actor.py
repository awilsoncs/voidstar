import random
from dataclasses import dataclass
from typing import List, Tuple

from components import TimedActor, Coordinates
from components.relationships.farmed_by import FarmedBy
from content.attacks import stab
from engine.core import log_debug


@dataclass
class PeasantActor(TimedActor):
    timer_delay = TimedActor.HALF_HOUR

    @log_debug(__name__)
    def act(self, scene):
        self.farm(scene)

    def farm(self, scene):
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

        stab_animation = stab(self.entity, target_tile[0], target_tile[1])
        scene.cm.add(*stab_animation[1])
        delay = random.randint(TimedActor.HALF_HOUR, TimedActor.DAILY)
        self.pass_turn(delay)
