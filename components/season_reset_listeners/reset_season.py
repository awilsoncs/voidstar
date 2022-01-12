from dataclasses import dataclass

from components.events.events import Event
from components.season_reset_listeners.seasonal_actor import SeasonResetListener


@dataclass
class ResetSeason(Event):
    # Season we're entering
    season: str = 'None'

    def listener_type(self):
        return SeasonResetListener

    def notify(self, scene, listener):
        listener.on_season_reset(scene, self.season)

    def _after_notify(self, scene):
        scene.message(f"{self.season} has begun.")
