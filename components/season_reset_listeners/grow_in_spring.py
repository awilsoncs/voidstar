from dataclasses import dataclass

from components import Coordinates
from components.actors.calendar_actor import Calendar
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from content.terrain.trees import make_tree
from engine import core


@dataclass
class GrowInSpring(SeasonResetListener):
    def on_season_reset(self, scene):
        calendar = scene.cm.get_one(Calendar, entity=core.get_id("calendar"))
        if not calendar:
            return

        if calendar.season == 1:
            coords = scene.cm.get_one(Coordinates, entity=self.entity)
            x = coords.x
            y = coords.y
            scene.cm.delete(self.entity)
            scene.cm.add(*make_tree(x, y)[1])
