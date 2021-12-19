from dataclasses import dataclass

from components.actors.calendar_actor import Calendar
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from engine import core


@dataclass
class DieInWinter(SeasonResetListener):
    def on_season_reset(self, scene):
        calendar = scene.cm.get_one(Calendar, entity=core.get_id("calendar"))
        if not calendar:
            return

        if calendar.season < 4:
            return

        scene.cm.delete(self.entity)
