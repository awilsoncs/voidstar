import logging
from dataclasses import dataclass

from components import Coordinates
from components.actors.calendar_actor import Calendar
from components.relationships.farmed_by import FarmedBy
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from content.crops import make_crops
from engine import core


@dataclass
class GrowCrops(SeasonResetListener):
    def on_season_reset(self, scene):
        calendar = scene.cm.get_one(Calendar, entity=core.get_id("calendar"))
        if not calendar:
            return

        if calendar.season > 2:
            return

        logging.info("Growing crops..")

        farmed_by = scene.cm.get_one(FarmedBy, entity=self.entity)
        farmer = farmed_by.farmer

        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        scene.cm.add(*make_crops(coords.x, coords.y, farmer, self.entity)[1])
