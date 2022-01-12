import logging
import random
from dataclasses import dataclass

import settings
from components import Coordinates
from components.build_world_listeners.build_world_listeners import BuildWorldListener
from components.build_world_listeners.world_parameters import WorldParameters
from content.terrain.rocks import make_rock
from engine import core
from engine.utilities import get_3_by_3_box


def add_rock(scene, x: int, y: int) -> None:
    coords = {(coord.x, coord.y) for coord in scene.cm.get(Coordinates)}
    if (x, y) not in coords:
        rock = make_rock(x, y)
        scene.cm.add(*rock[1])


@dataclass
class PlaceRocks(BuildWorldListener):
    def on_build_world(self, scene):
        self._log_info(f"placing rock fields in town...")
        world_settings = scene.cm.get_one(WorldParameters, entity=core.get_id("world"))
        for _ in range(world_settings.rock_fields):
            x = random.randint(0, settings.MAP_WIDTH - 1)
            y = random.randint(0, settings.MAP_HEIGHT - 1)
            coords = {(coord.x, coord.y) for coord in scene.cm.get(Coordinates)}
            if (x, y) not in coords:
                self.add_rock_field(scene, x, y)

    def add_rock_field(self, scene, x: int, y: int) -> None:
        world_settings = scene.cm.get_one(WorldParameters, entity=core.get_id("world"))
        working_set = [(x, y)]
        maximum = 10
        while working_set and maximum > 0:
            working_x, working_y = working_set.pop(0)
            add_rock(scene, working_x, working_y)
            maximum -= 1
            working_set += [
                (_x, _y)
                for _x, _y in get_3_by_3_box(working_x, working_y)
                if (
                        random.random() <= world_settings.rocks_proliferation
                        and 0 < _x < settings.MAP_WIDTH - 1
                        and 0 < _y < settings.MAP_HEIGHT - 1
                )
            ]
