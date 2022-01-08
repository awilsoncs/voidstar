import logging
import random
from dataclasses import dataclass

import settings
from components import Coordinates
from components.build_world_listeners.build_world_listeners import BuildWorldListener
from components.build_world_listeners.world_parameters import WorldParameters
from content.terrain.trees import make_tree
from engine.utilities import get_3_by_3_box


def add_tree(scene, x: int, y: int) -> None:
    coords = {(coord.x, coord.y) for coord in scene.cm.get(Coordinates)}
    if (x, y) not in coords:
        tree = make_tree(x, y)
        scene.cm.add(*tree[1])


@dataclass
class PlaceTrees(BuildWorldListener):
    def on_build_world(self, scene):
        logging.info(f"EID#{self.entity}::PlaceTrees placing trees in town")
        world_settings = scene.cm.get_one(WorldParameters, entity=scene.player)

        for _ in range(world_settings.copse):
            x = random.randint(0, settings.MAP_WIDTH - 1)
            y = random.randint(0, settings.MAP_HEIGHT - 1)
            coords = {(coord.x, coord.y) for coord in scene.cm.get(Coordinates)}
            if (x, y) not in coords:
                self.spawn_copse(scene, x, y)

    def spawn_copse(self, scene, x: int, y: int) -> None:
        world_settings = scene.cm.get_one(WorldParameters, entity=scene.player)
        working_set = [(x, y)]
        maximum = 10
        while working_set and maximum > 0:
            working_x, working_y = working_set.pop(0)
            add_tree(scene, working_x, working_y)
            maximum -= 1
            working_set += [
                (_x, _y)
                for _x, _y in get_3_by_3_box(working_x, working_y)
                if (
                        random.random() <= world_settings.copse_proliferation
                        and 0 < _x < settings.MAP_WIDTH - 1
                        and 0 < _y < settings.MAP_HEIGHT - 1
                )
            ]
