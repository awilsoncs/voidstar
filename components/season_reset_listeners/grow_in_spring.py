import logging
from dataclasses import dataclass
import random

from components import Coordinates
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from components.weather.weather import Weather
from content.terrain.trees import make_tree


@dataclass
class GrowIntoTree(SeasonResetListener):
    def on_season_reset(self, scene, season):
        weather = scene.cm.get(Weather)
        if weather:
            weather = weather[0]
        else:
            logging.warning(f"EID#{self.entity}::GrowIntoTree no weather found")
            return

        if random.randint(0, 200) < weather.seasonal_norm:
            coords = scene.cm.get_one(Coordinates, entity=self.entity)
            x = coords.x
            y = coords.y
            scene.cm.delete(self.entity)
            scene.cm.add(*make_tree(x, y)[1])
