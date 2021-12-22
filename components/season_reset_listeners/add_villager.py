from dataclasses import dataclass

from components.actors.calendar_actor import Calendar
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from content.farmsteads.houses import place_farmstead


@dataclass
class AddVillager(SeasonResetListener):
    def on_season_reset(self, scene):
        calendar = scene.cm.get_one(Calendar, entity=self.entity)
        if calendar.season == 1:
            place_farmstead(scene)
