import random
from dataclasses import dataclass

import settings
from engine.components.energy_actor import EnergyActor
from content.enemies.juggernaut import make_juggernaut
from content.enemies.juvenile import make_juvenile
from content.enemies.pirhana import make_pirhana
from content.enemies.sneaker import make_sneaker


@dataclass
class HordelingSpawner(EnergyActor):
    """Hordelings will spawn at this object's location."""
    energy_cost: int = EnergyActor.HOURLY
    waves: int = 1

    def act(self, scene):
        spawn_hordeling(scene)
        self.pass_turn(random.randint(EnergyActor.QUARTER_HOUR, EnergyActor.HOURLY*20))

        self.waves -= 1

        if self.waves <= 0:
            scene.cm.delete(self.entity)


def spawn_hordeling(scene):
    """Add a hordeling spawner to a random edge of the map."""
    x, y = get_wall_coords()
    roll = random.random()
    if roll > .8:
        maker = random.choice([make_sneaker, make_juggernaut, make_pirhana])
        scene.cm.add(*maker(x, y)[1])
    else:
        scene.cm.add(*make_juvenile(x, y)[1])


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
