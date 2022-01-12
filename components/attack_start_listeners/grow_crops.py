from dataclasses import dataclass
from typing import Tuple

from components import Coordinates
from components.actors.calendar_actor import Calendar
from components.events.attack_started_events import AttackStartListener
from components.relationships.farmed_by import FarmedBy
from components.tags.crop_info import CropInfo
from content.farmsteads.crops import make_crops
from engine import core, palettes


@dataclass
class GrowCrops(AttackStartListener):
    crop_color: Tuple = palettes.FIRE

    def on_attack_start(self, scene):
        calendar = scene.cm.get_one(Calendar, entity=core.get_id("calendar"))
        if not calendar:
            return

        if calendar.season > 2:
            return

        crop_info = scene.cm.get(CropInfo, query=lambda ci: ci.field_id == self.entity)
        if crop_info:
            return

        self._log_info(f"growing crops")

        farmed_by = scene.cm.get_one(FarmedBy, entity=self.entity)
        farmer = farmed_by.farmer

        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        scene.cm.add(*make_crops(coords.x, coords.y, farmer, self.entity, self.crop_color)[1])
