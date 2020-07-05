import random
from dataclasses import dataclass

import settings
from components import TimedActor
from content.enemies import make_hordeling
from systems.utilities import retract_turn


@dataclass
class HordelingSpawner(TimedActor):
    """Hordelings will spawn at this object's location."""

    def act(self, scene):
        if random.randint(1, 100) < settings.SPAWN_FREQUENCY:

            x = random.randint(0, settings.MAP_WIDTH - 1)

            scene.cm.add(*make_hordeling(x, 0)[1])
        retract_turn(scene, self.entity)
