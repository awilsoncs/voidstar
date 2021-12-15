import random
from dataclasses import dataclass

import settings
from components import Coordinates
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from content.structures.houses import make_peasant_home
from engine.utilities import get_3_by_3_square


@dataclass
class AddVillager(SeasonResetListener):
    def on_season_reset(self, scene):
        suitable_location = False
        taken_coords = {c.position for c in scene.cm.get(Coordinates)}

        while not suitable_location:
            x = random.randint(5, settings.MAP_WIDTH - 5)
            y = random.randint(5, settings.MAP_HEIGHT - 5)
            home_footprint = get_3_by_3_square(x, y)
            if home_footprint.isdisjoint(taken_coords):
                migrant = make_peasant_home(x, y)
                for entity in migrant:
                    scene.cm.add(*entity[1])
            suitable_location = True

