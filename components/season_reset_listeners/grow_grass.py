from dataclasses import dataclass

from components.actors.calendar_actor import Calendar
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from engine import core


@dataclass
class GrowGrass(SeasonResetListener):
    def on_season_reset(self, scene, season):
        if season in {'Spring', 'Summer'}:
            scene.cm.delete(self.entity)
