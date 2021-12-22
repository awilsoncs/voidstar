from dataclasses import dataclass

from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from content.farmsteads.houses import place_farmstead


@dataclass
class AddVillager(SeasonResetListener):
    def on_season_reset(self, scene):
        place_farmstead(scene)


