import random
from dataclasses import dataclass

import settings
from components import TimedActor, Coordinates
from content.enemies import make_hordeling
from content.spawners.hordeling_spawner import hordeling_spawner
from systems.utilities import retract_turn


@dataclass
class HordelingSpawnerSpawner(TimedActor):
    """Hordelings will spawn at this object's location."""
    timer_delay: int = TimedActor.DAILY
    level: int = 1

    def act(self, scene):
        for _ in range(self.level):
            spawn_hordeling_spawner(scene)
        retract_turn(scene, self.entity)


def spawn_hordeling_spawner(scene):
    """Add a hordeling spawner to a random edge of the map."""
    x, y = get_wall_coords()
    scene.cm.add(*hordeling_spawner(x=x, y=y)[1])


def get_wall_coords():
    return random.choice(
        [
            (get_random_width_location(), 0),
            (0, get_random_height_location()),
            (settings.MAP_WIDTH - 1, get_random_height_location()),
            (get_random_width_location(), settings.MAP_HEIGHT - 1)
        ]
    )


def get_random_width_location():
    return random.randrange(1, settings.MAP_WIDTH - 1)


def get_random_height_location():
    return random.randrange(1, settings.MAP_HEIGHT - 1)