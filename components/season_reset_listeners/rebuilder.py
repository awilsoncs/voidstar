from dataclasses import dataclass
from typing import Optional

from components import Coordinates
from components.residence import Residence
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from components.house_structure import HouseStructure
from components.owner import Owner
from content.houses import make_wall


@dataclass
class Rebuilder(SeasonResetListener):
    """Rebuilds broken down house walls."""
    def on_season_reset(self, scene):
        if self._is_resident_alive(scene):
            self._rebuild_house(scene)
        else:
            # https://www.youtube.com/watch?v=4KoiYEoWImo
            scene.cm.delete(self.entity)

    def _is_resident_alive(self, scene) -> bool:
        house_structure: Optional[HouseStructure] = self._get_house_structure(scene)
        if not house_structure:
            raise NotImplementedError("Cannot handle resident with missing house structure")
        house_id = house_structure.house_id
        residences = scene.cm.get(Residence)
        return any(residence.house_id == house_id for residence in residences)

    def _rebuild_house(self, scene):
        house_structure = self._get_house_structure(scene)
        house_id = house_structure.house_id
        coords = scene.cm.get_one(Coordinates, entity=house_structure.entity)
        x = coords.x
        y = coords.y
        upper_left = make_wall(house_id, x - 1, y - 1)
        upper_middle = make_wall(house_id, x, y - 1)
        upper_right = make_wall(house_id, x + 1, y - 1)
        middle_left = make_wall(house_id, x - 1, y)
        middle_right = make_wall(house_id, x + 1, y)
        bottom_left = make_wall(house_id, x - 1, y + 1)
        bottom_middle = make_wall(house_id, x, y + 1)
        bottom_right = make_wall(house_id, x + 1, y + 1)
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

    def _get_house_structure(self, scene) -> Optional[HouseStructure]:
        house_link = scene.cm.get_one(Owner, entity=self.entity)
        if not house_link:
            raise NotImplementedError("cannot yet handle rebuilder without parent entity")
        house_id = house_link.owner
        house_structures = [hs for hs in scene.cm.get(HouseStructure) if hs.house_id == house_id]
        assert len(house_structures) == 1, "can only have one house structure"
        house_structure = house_structures.pop()
        return house_structure
