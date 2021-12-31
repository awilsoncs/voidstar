from dataclasses import dataclass

from components.actors.calendar_actor import Calendar
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from components.tags.crop_info import CropInfo
from engine import core, palettes


@dataclass
class CropsDieInWinter(SeasonResetListener):
    def on_season_reset(self, scene, season):
        if season == 'Winter':
            scene.message("The peasants harvested the last of the crops before frost set in.", color=palettes.WATER)
            crops = scene.cm.get(CropInfo, project=lambda ci: ci.entity)
            for crop in crops:
                scene.cm.delete(crop)
