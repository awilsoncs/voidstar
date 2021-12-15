import random
from itertools import product

import settings
from components import Coordinates
from content.debug_enemies import make_debug_hordeling
from content.structures.houses import make_peasant_home
from content.player import make_player
from engine import core
from engine.utilities import get_3_by_3_square


class DebugFieldBuilder:
    """Generate a debug dungeon."""

    def __init__(self, peasants):
        self.object_map = {}
        self.tile_map = {}
        self.cm = None
        self.zone_id = core.get_id()
        self.noise_generator = core.get_noise_generator()
        self.peasants = peasants

    def build(self, cm):
        self.make_world(cm, 1)

    def make_world(self, cm, zone_id):
        """Create a component manager containing the initial map."""
        self.cm = cm
        self.zone_id = zone_id

        self.create_player(settings.MAP_HEIGHT // 2, settings.MAP_WIDTH // 2)
        self.place_objects()
        return self.cm

    def create_player(self, x, y):
        player = make_player(self.zone_id)
        player[1].append(
            Coordinates(entity=player[0], x=x, y=y),
        )
        self.cm.add(*player[1])

    def add_house(self, x, y):
        house = make_peasant_home(x, y)
        for entity in house:
            self.cm.add(*entity[1])
            for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
                self.object_map[x+dx, y+dy] = entity[0]

    def place_objects(self):
        for i in range(10):
            x = random.randint(5, settings.MAP_WIDTH - 5)
            y = random.randint(5, settings.MAP_HEIGHT - 5)
            hordeling = make_debug_hordeling(x, y)
            self.cm.add(*hordeling[1])
            self.object_map[x, y] = hordeling[0]

        while self.peasants > 0:
            x = random.randint(5, settings.MAP_WIDTH - 5)
            y = random.randint(5, settings.MAP_HEIGHT - 5)
            footprint = get_3_by_3_square(x, y)

            disjoint = self.object_map.keys().isdisjoint(footprint)
            if disjoint:
                self.add_house(x, y)
                self.peasants -= 1
