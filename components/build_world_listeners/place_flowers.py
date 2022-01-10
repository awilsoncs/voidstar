import logging
from dataclasses import dataclass
import random

import settings
from components import Coordinates
from components.build_world_listeners.build_world_listeners import BuildWorldListener
from components.build_world_listeners.world_parameters import WorldParameters
from content.terrain.flower import make_flower
from engine import palettes
from engine.utilities import get_3_by_3_box


def add_flower(scene, x: int, y: int, color) -> None:
    coords = {(coord.x, coord.y) for coord in scene.cm.get(Coordinates)}
    if (x, y) not in coords:
        flower = make_flower(x, y, color)
        scene.cm.add(*flower[1])


@dataclass
class PlaceFlowers(BuildWorldListener):
    color = None

    def on_build_world(self, scene):
        logging.info(f"EID#{self.entity}::PlaceFlowers placing flower fields...")
        world_settings = scene.cm.get_one(WorldParameters, entity=scene.player)
        self.color = random.choice([palettes.WHITE, palettes.WATER, palettes.FRESH_BLOOD, palettes.FIRE, palettes.GOLD])
        for _ in range(world_settings.flower_fields):
            x = random.randint(0, settings.MAP_WIDTH - 1)
            y = random.randint(0, settings.MAP_HEIGHT - 1)
            coords = {(coord.x, coord.y) for coord in scene.cm.get(Coordinates)}
            if (x, y) not in coords:
                self.add_flower_field(scene, x, y)

    def add_flower_field(self, scene, x: int, y: int) -> None:
        world_settings = scene.cm.get_one(WorldParameters, entity=scene.player)
        working_set = [(x, y)]
        maximum = 10
        while working_set and maximum > 0:
            working_x, working_y = working_set.pop(0)
            add_flower(scene, working_x, working_y, self.color)
            maximum -= 1
            working_set += [
                (_x, _y)
                for _x, _y in get_3_by_3_box(working_x, working_y)
                if (
                        random.random() <= world_settings.flower_proliferation
                        and 0 < _x < settings.MAP_WIDTH - 1
                        and 0 < _y < settings.MAP_HEIGHT - 1
                )
            ]
