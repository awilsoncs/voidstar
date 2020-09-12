import random
from dataclasses import dataclass, field

import settings
from components import TimedActor, Coordinates
from content.enemies import make_hordeling
from systems.utilities import retract_turn


def get_hordeling_count():
    return random.randint(settings.SPAWN_MIN, settings.SPAWN_MAX)


@dataclass
class HordelingSpawner(TimedActor):
    """Hordelings will spawn at this object's location."""
    remaining: int = field(default_factory=get_hordeling_count)
    timer_delay: int = TimedActor.QUARTER_HOUR

    def act(self, scene):
        if random.randint(1, 100) < settings.SPAWN_FREQUENCY:

            coords = scene.cm.get_one(Coordinates, entity=self.entity)
            assert coords, "no coords found for spawner"

            scene.cm.add(*make_hordeling(coords.x, coords.y)[1])
            self.remaining -= 1
        retract_turn(scene, self.entity)

        if self.remaining <= 0:
            scene.cm.delete(self.entity)
