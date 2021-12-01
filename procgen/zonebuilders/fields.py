import random
from itertools import product

import settings
from components import Coordinates
from content.allies import make_peasant
from content.houses import make_house
from content.player import make_player
from content.terrain import make_tree, make_water
from engine import core
from engine.component_manager import ComponentManager
from engine.constants import PRIORITY_MEDIUM
from engine.utilities import get_3_by_3_square


def build(cm: ComponentManager, zone_id: int, peasants):
    return FieldBuilder(peasants).make_world(cm, zone_id)


class FieldBuilder:
    """Generate a generic dungeon."""

    def __init__(self, peasants):
        self.object_map = {}
        self.tile_map = {}
        self.cm = None
        self.zone_id = core.get_id()
        self.noise_generator = core.get_noise_generator()
        self.peasants = peasants

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

    def spawn_copse(self, x: int, y: int) -> None:
        working_set = [(x, y)]
        maximum = 10
        while working_set and maximum > 0:
            working_x, working_y = working_set.pop()
            self.add_tree(working_x, working_y)
            maximum -= 1
            for dx, dy in [
                p
                for p in product([-1, 0, 1], [-1, 0, 1])
                if p != (0, 0) and random.random() <= settings.COPSE_PROLIFERATION
            ]:
                next_x = working_x + dx
                next_y = working_y + dy
                if (
                    1 < next_x < settings.MAP_WIDTH - 1
                    and 1 < next_y < settings.MAP_HEIGHT - 1
                ):
                    working_set.append(
                        (next_x, next_y)
                    )

    def add_tree(self, x: int, y: int) -> None:
        tree = make_tree(self.zone_id)
        tree[1].append(
            Coordinates(
                entity=tree[0],
                x=x,
                y=y,
                priority=PRIORITY_MEDIUM,
                terrain=True,
            )
        )
        self.cm.add(*tree[1])
        self.object_map[x, y] = tree[0]

    def spawn_body_water(self, x: int, y: int) -> None:
        working_set = [(x, y)]
        maximum = 50
        while working_set and maximum > 0:
            working_x, working_y = working_set.pop()
            self.add_water(working_x, working_y)
            maximum -= 1
            for dx, dy in [
                p
                for p in product([-1, 0, 1], [-1, 0, 1])
                if p != (0, 0) and random.random() <= settings.LAKE_PROLIFERATION
            ]:
                next_x = working_x + dx
                next_y = working_y + dy
                if (
                    1 < next_x < settings.MAP_WIDTH - 1
                    and 1 < next_y < settings.MAP_HEIGHT - 1
                ):
                    working_set.append(
                        (next_x, next_y)
                    )

    def add_water(self, x: int, y: int) -> None:
        water = make_water(x, y)
        self.cm.add(*water[1])
        self.object_map[x, y] = water[0]

    def add_peasant(self, x, y):
        peasant = make_peasant(self.zone_id, x, y)
        self.cm.add(*peasant[1])
        self.object_map[x, y] = peasant[0]
        self.peasants -= 1

    def add_house(self, x, y):
        house = make_house(self.zone_id, x, y)
        for wall in house:
            self.cm.add(*wall[1])
            self.object_map[x, y] = wall[0]

    def place_objects(self):
        for x in range(0, settings.MAP_WIDTH - 1):
            self.add_tree(x, 0)
            self.add_tree(x, settings.MAP_HEIGHT - 1)

        for y in range(1, settings.MAP_HEIGHT - 1):
            self.add_tree(0, y)
            self.add_tree(settings.MAP_WIDTH - 1, y)

        while self.peasants > 0:
            x = random.randint(5, settings.MAP_WIDTH - 5)
            y = random.randint(5, settings.MAP_HEIGHT - 5)
            footprint = get_3_by_3_square(x, y)

            disjoint = self.object_map.keys().isdisjoint(footprint)
            if disjoint:
                self.add_house(x, y)
                self.add_peasant(x, y)

        for _ in range(random.randint(settings.COPSE_MIN, settings.COPSE_MAX)):
            x = random.randint(0, settings.MAP_WIDTH - 1)
            y = random.randint(0, settings.MAP_HEIGHT - 1)
            if (x, y) not in self.object_map:
                self.spawn_copse(x, y)

        for _ in range(random.randint(settings.LAKES_MIN, settings.LAKES_MAX)):
            x = random.randint(0, settings.MAP_WIDTH - 1)
            y = random.randint(0, settings.MAP_HEIGHT - 1)
            if (x, y) not in self.object_map:
                self.spawn_body_water(x, y)

