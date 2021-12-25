import logging
import random
from typing import List

from components import Coordinates
from components.build_world_listeners.build_world_listeners import BuildWorldListener
from components.house_structure import HouseStructure
from components.tags.town_center_flag import TownCenterFlag
from content.terrain.roads import make_road, connect_point_to_road_network
from engine.utilities import get_3_by_3_square, get_3_by_3_box


def get_town_center(house_coords, scene):
    avg_x = int(sum(c.x for c in house_coords) / len(house_coords))
    avg_y = int(sum(c.y for c in house_coords) / len(house_coords))
    all_coords = set(scene.cm.get(Coordinates, project=lambda c: (c.x, c.y)))
    while not get_3_by_3_square(avg_x, avg_y).isdisjoint(all_coords):
        # perturb until we find a random spot
        avg_x += random.randint(-2, 2)
        avg_y += random.randint(-2, 2)
    return avg_x, avg_y


class PlaceRoads(BuildWorldListener):
    def on_build_world(self, scene):
        logging.info(f"EID#{self.entity}::PlaceRoads placing roads in town")
        houses: List[HouseStructure] = scene.cm.get(HouseStructure, project=lambda hs: hs.house_id)
        house_coords: List[Coordinates] = [scene.cm.get_one(Coordinates, entity=house) for house in houses]

        # Identify the town center by averaging the coords
        avg_x, avg_y = get_town_center(house_coords, scene)

        for coord in list(get_3_by_3_box(avg_x, avg_y)):
            scene.cm.add(*make_road(coord[0], coord[1])[1])

        town_center = make_road(avg_x, avg_y)
        town_center[1].append(TownCenterFlag(entity=town_center[0]))
        scene.cm.add(*town_center[1])

        for coord in house_coords:
            connect_point_to_road_network(scene, coord.position)
