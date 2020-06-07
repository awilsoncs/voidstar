import random

import settings
from components import Appearance, Coordinates
from content.allies import make_peasant
from content.enemies import make_hordeling
from content.gold import make_gold_nugget
from content.player import make_player
from content.terrain import make_tree, make_water
from engine import core, palettes
from engine.component_manager import ComponentManager
from engine.constants import PRIORITY_LOWEST, PRIORITY_MEDIUM
from engine.palettes import Palette
from settings import MAP_HEIGHT, MAP_WIDTH


def build(cm: ComponentManager, zone_id: int, peasants, monsters):
    return FieldBuilder(peasants, monsters).make_world(cm, zone_id)


class FieldBuilder:
    """Generate a generic dungeon."""

    def __init__(self, peasants, monsters):
        self.object_map = {}
        self.tile_map = {}
        self.cm = None
        self.zone_id = core.get_id()
        self.palette = Palette()
        self.noise_generator = core.get_noise_generator()
        self.mob_color = palettes.white
        self.peasants = peasants
        self.monsters = monsters

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

    def add_water(self, x: int, y: int) -> None:
        tree = make_water(self.zone_id)
        tree[1].append(
            Coordinates(
                entity=tree[0],
                x=x,
                y=y,
                priority=PRIORITY_LOWEST,
                terrain=True,
            )
        )
        self.cm.add(*tree[1])
        self.object_map[x, y] = tree[0]

    def add_hordeling(self, x, y):
        hordeling = make_hordeling(self.zone_id)
        hordeling[1].append(
            Coordinates(
                entity=hordeling[0],
                x=x,
                y=y,
                priority=PRIORITY_MEDIUM,
                terrain=False,
            )
        )
        self.cm.add(*hordeling[1])
        self.object_map[x, y] = hordeling[0]
        self.monsters -= 1

    def add_peasant(self, x, y):
        peasant = make_peasant(self.zone_id)
        peasant[1].append(
            Coordinates(
                entity=peasant[0],
                x=x,
                y=y,
                priority=PRIORITY_MEDIUM,
                terrain=False,
            )
        )
        self.cm.add(*peasant[1])
        self.object_map[x, y] = peasant[0]
        self.peasants -= 1

    def place_objects(self):
        for x in range(0, settings.MAP_WIDTH - 1):
            self.add_tree(x, 0)
            self.add_tree(x, settings.MAP_HEIGHT - 1)

        for y in range(1, settings.MAP_HEIGHT - 1):
            self.add_tree(0, y)
            self.add_tree(settings.MAP_WIDTH - 1, y)

        for _ in range(50):
            x = random.randint(0, settings.MAP_WIDTH - 1)
            y = random.randint(0, settings.MAP_HEIGHT - 1)
            if (x, y) not in self.object_map:
                self.add_tree(x, y)

        for _ in range(20):
            x = random.randint(0, settings.MAP_WIDTH - 1)
            y = random.randint(0, settings.MAP_HEIGHT - 1)
            if (x, y) not in self.object_map:
                self.add_water(x, y)

        if random.randint(1, 3) == 3:
            x = random.randint(0, settings.MAP_WIDTH - 1)
            y = random.randint(0, settings.MAP_HEIGHT - 1)
            if (x, y) not in self.object_map:
                gold_nugget = make_gold_nugget(x, y)
                self.object_map[x, y] = gold_nugget[0]
                self.cm.add(*gold_nugget[1])

        while self.monsters > 0:
            x = random.randint(0, settings.MAP_WIDTH - 1)
            y = random.randint(0, settings.MAP_HEIGHT - 1)
            if (x, y) not in self.object_map:
                self.add_hordeling(x, y)

        while self.peasants > 0:
            x = random.randint(0, settings.MAP_WIDTH - 1)
            y = random.randint(0, settings.MAP_HEIGHT - 1)
            if (x, y) not in self.object_map:
                self.add_peasant(x, y)
