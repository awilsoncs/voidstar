from dataclasses import dataclass, field
import random

from components import Coordinates
from components.events.new_day_event import DayBeganListener
from components.weather.weather import Weather
from content.terrain.trees import make_tree


def temperature_time_to_grow():
    return random.randint(1200, 3600)


@dataclass
class GrowIntoTree(DayBeganListener):
    time_to_grow: int = field(default_factory=temperature_time_to_grow)

    def on_new_day(self, scene, day):
        weather = scene.cm.get(Weather)
        if weather:
            weather = weather[0]
        else:
            self._log_warning(f"no weather found")
            return

        self.time_to_grow = max(0, self.time_to_grow - max(0, weather.temperature))

        if self.time_to_grow <= 0:
            self._log_debug("sapling growing into a tree")
            coords = scene.cm.get_one(Coordinates, entity=self.entity)
            x = coords.x
            y = coords.y
            scene.cm.delete(self.entity)
            scene.cm.add(*make_tree(x, y)[1])
