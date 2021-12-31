import logging
from dataclasses import dataclass
from typing import List

from components import Coordinates
from components.relationships.farmed_by import FarmedBy
from components.relationships.resident import Resident
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from components.house_structure import HouseStructure
from components.tags.peasant_tag import PeasantTag
from content.farmsteads.walls import make_wall


@dataclass
class Rebuilder(SeasonResetListener):
    """Rebuild during a season reset if the resident is still alive. Otherwise, delete."""

    def on_season_reset(self, scene, season):
        house_structure = scene.cm.get_one(HouseStructure, entity=self.entity)
        if house_structure and house_structure.is_destroyed:
            if self._get_living_residents(scene):
                self._rebuild_house(scene)
            else:
                self._delete_farms(scene)

                # https://www.youtube.com/watch?v=4KoiYEoWImo
                scene.cm.delete(self.entity)

    def _get_living_residents(self, scene) -> List[PeasantTag]:
        resident: Resident = scene.cm.get_one(Resident, entity=self.entity)
        peasants: List[PeasantTag] = scene.cm.get(PeasantTag, query=lambda pt: pt.entity == resident.resident)
        return peasants

    def _rebuild_house(self, scene):
        house_structure = scene.cm.get_one(HouseStructure, entity=self.entity)
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        x = coords.x
        y = coords.y
        upper_left = make_wall(self.entity, x - 1, y - 1, piece='ul')
        upper_middle = make_wall(self.entity, x, y - 1, piece='um')
        upper_right = make_wall(self.entity, x + 1, y - 1, piece='ur')
        middle_left = make_wall(self.entity, x - 1, y, piece='ml')
        middle_right = make_wall(self.entity, x + 1, y, piece='mr')
        bottom_left = make_wall(self.entity, x - 1, y + 1, piece='bl')
        bottom_middle = make_wall(self.entity, x, y + 1, piece='bm')
        bottom_right = make_wall(self.entity, x + 1, y + 1, piece='br')
        house_structure.upper_left = upper_left[0]
        house_structure.upper_middle = upper_middle[0]
        house_structure.upper_right = upper_right[0]
        house_structure.middle_left = middle_left[0]
        house_structure.middle_right = middle_right[0]
        house_structure.bottom_left = bottom_left[0]
        house_structure.bottom_middle = bottom_middle[0]
        house_structure.bottom_right = bottom_right[0]
        for wall in [
            upper_left, upper_middle, upper_right,
            middle_left, middle_right,
            bottom_left, bottom_middle, bottom_right
        ]:
            scene.cm.add(*wall[1])

        house_structure.is_destroyed = False

    def _delete_farms(self, scene):
        logging.debug(f"Deleting farms for house #{self.entity}")
        resident_link: Resident = scene.cm.get_one(Resident, entity=self.entity)
        if not resident_link:
            logging.warning("House with no historical resident found, should not happen")
            return
        else:
            resident_id = resident_link.resident

        farms: List[int] = scene.cm.get(
            FarmedBy,
            query=lambda fb: fb.farmer == resident_id,
            project=lambda fb: fb.entity
        )

        for farm in farms:
            logging.debug(f"Deleting farm #{farm}")
            scene.cm.delete(farm)
