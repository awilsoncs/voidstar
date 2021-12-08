from dataclasses import dataclass

from components.season_reset_listeners.seasonal_actor import SeasonResetListener


@dataclass
class ShootAbility(SeasonResetListener):
    count: int = 5
    max: int = 5

    def on_season_reset(self, scene):
        self.count = self.max
