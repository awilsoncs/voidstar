import logging
import random
from dataclasses import dataclass

from components import Coordinates
from components.actors.calendar_actor import Calendar
from components.attack_start_listeners.attack_start_actor import AttackStartListener
from components.relationships.farmed_by import FarmedBy
from content.farmsteads.crops import make_crops
from engine import core


@dataclass
class GrowCrops(AttackStartListener):

    def on_attack_start(self, scene):
        calendar = scene.cm.get_one(Calendar, entity=core.get_id("calendar"))
        if not calendar:
            return

        if calendar.season > 2:
            return

        if random.random() < .3:

            logging.info(f"EID#{self.entity}::GrowCrops: Growing crops..")

            farmed_by = scene.cm.get_one(FarmedBy, entity=self.entity)
            farmer = farmed_by.farmer

            coords = scene.cm.get_one(Coordinates, entity=self.entity)
            scene.cm.add(*make_crops(coords.x, coords.y, farmer, self.entity)[1])
