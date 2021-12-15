import logging
from dataclasses import dataclass
import random

import settings
from components import Coordinates
from components.build_world_listeners.build_world_listeners import BuildWorldListener
from content.structures.houses import make_peasant_home
from engine.utilities import get_3_by_3_square


def add_house(scene, x, y):
    house = make_peasant_home(x, y)
    for entity in house:
        scene.cm.add(*entity[1])


@dataclass
class PlacePeasants(BuildWorldListener):
    def on_build_world(self, scene):
        logging.info("Placing peasants...")
        peasants = 3
        while peasants > 0:
            x = random.randint(5, settings.MAP_WIDTH - 5)
            y = random.randint(5, settings.MAP_HEIGHT - 5)
            footprint = get_3_by_3_square(x, y)

            coords = {(coord.x, coord.y) for coord in scene.cm.get(Coordinates)}
            if coords.isdisjoint(footprint):
                add_house(scene, x, y)
                peasants -= 1
