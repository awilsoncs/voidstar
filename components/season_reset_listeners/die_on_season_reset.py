from dataclasses import dataclass

from components.events.die_events import Die
from components.season_reset_listeners.seasonal_actor import SeasonResetListener


@dataclass
class DieOnSeasonReset(SeasonResetListener):
    def on_season_reset(self, scene, season):
        scene.cm.add(Die(entity=self.entity, killer=self.entity))
