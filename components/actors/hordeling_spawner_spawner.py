import random
from dataclasses import dataclass

import settings
from components import TimedActor
from components.actors.energy_actor import EnergyActor
from content.spawners.hordeling_spawner import hordeling_spawner


@dataclass
class HordelingSpawnerSpawner(EnergyActor):
    """Hordelings will spawn at this object's location."""
    timer_delay: int = TimedActor.SIX_SECONDS
    energy_cost: int = EnergyActor.HOURLY
    waves: int = 1

    def act(self, scene):
        spawn_hordeling_spawner(scene)
        self.pass_turn()

        self.waves -= 1

        if self.waves <= 0:
            scene.cm.delete(self.entity)


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
