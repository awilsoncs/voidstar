import random
from dataclasses import dataclass

import settings
from components import Coordinates
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from components.relationships.farmed_by import FarmedBy
from content.terrain.farms import make_farm_plot


def get_random_point():
    x = random.randint(1, settings.MAP_WIDTH - 1)
    y = random.randint(1, settings.MAP_HEIGHT - 1)
    return x, y


def start_new_farm(farmer, scene):
    taken_coords = {(coords.x, coords.y) for coords in scene.cm.get(Coordinates)}
    try_point = get_random_point()
    while try_point in taken_coords:
        try_point = get_random_point()
    plot = make_farm_plot(try_point[0], try_point[1], farmer)
    scene.cm.add(*plot[1])


@dataclass
class PlantFarm(SeasonResetListener):
    def on_season_reset(self, scene):
        farmer = self.entity
        farm_coords = scene.cm.get(FarmedBy, query=lambda x: x.farmer == farmer)
        if farm_coords:
            pass
        else:
            start_new_farm(farmer, scene)
