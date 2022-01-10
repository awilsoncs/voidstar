import logging
import random
from dataclasses import dataclass

import settings
from components import Coordinates
from components.build_world_listeners.build_world_listeners import BuildWorldListener
from components.build_world_listeners.world_parameters import WorldParameters
from content.terrain.water import make_water, make_swampy_water
from engine.utilities import get_3_by_3_box


def add_water(scene, x: int, y: int, painter) -> None:
    coords = {(coord.x, coord.y) for coord in scene.cm.get(Coordinates)}
    if (x, y) not in coords:
        water = painter(x, y)
        scene.cm.add(*water[1])


@dataclass
class PlaceLakes(BuildWorldListener):
    def on_build_world(self, scene):
        logging.info(f"EID#{self.entity}::PlaceLakes placing lakes in town")
        world_settings = scene.cm.get_one(WorldParameters, entity=scene.player)

        for _ in range(world_settings.lakes):
            x = random.randint(0, settings.MAP_WIDTH - 1)
            y = random.randint(0, settings.MAP_HEIGHT - 1)
            coords = {(coord.x, coord.y) for coord in scene.cm.get(Coordinates)}
            if (x, y) not in coords:
                self.spawn_lake(scene, x, y)

    def spawn_lake(self, scene, x: int, y: int) -> None:
        working_set = [(x, y)]
        maximum = 50
        world_settings = scene.cm.get_one(WorldParameters, entity=scene.player)
        if world_settings.is_water_swampy:
            water_painter = make_swampy_water
        else:
            water_painter = make_water

        while working_set and maximum > 0:
            working_x, working_y = working_set.pop(0)
            add_water(scene, working_x, working_y, water_painter)
            maximum -= 1
            working_set += [
                (_x, _y)
                for _x, _y in get_3_by_3_box(working_x, working_y)
                if (
                        random.random() <= world_settings.lake_proliferation
                        and 0 < _x < settings.MAP_WIDTH
                        and 0 < _y < settings.MAP_HEIGHT
                )
            ]
