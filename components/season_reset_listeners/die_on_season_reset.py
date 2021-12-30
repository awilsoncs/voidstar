from dataclasses import dataclass

from components.death_listeners.die import Die
from components.season_reset_listeners.seasonal_actor import SeasonResetListener


@dataclass
class DieOnSeasonReset(SeasonResetListener):
    def on_season_reset(self, scene):
        scene.cm.add(Die(entity=self.entity))
