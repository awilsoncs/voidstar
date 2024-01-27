import random
from typing import List

import settings
from components import Coordinates
from components.events.build_world_events import BuildWorldListener
from components.tags.town_center_flag import TownCenterFlag
from content.terrain.roads import make_road, connect_point_to_road_network
from engine.utilities import get_3_by_3_box


def get_town_center(house_coords, scene):
    return settings.MAP_WIDTH // 2, settings.MAP_HEIGHT // 2


def add_town_center(house_coords, scene):
    # Identify the town center by averaging the coords
    avg_x, avg_y = get_town_center(house_coords, scene)
    for coord in list(get_3_by_3_box(avg_x, avg_y)):
        scene.cm.add(*make_road(coord[0], coord[1])[1])
    town_center = make_road(avg_x, avg_y)
    town_center[1].append(TownCenterFlag(entity=town_center[0]))
    scene.cm.add(*town_center[1])


class PlaceRoads(BuildWorldListener):
    def on_build_world(self, scene):
        self._log_info(f"placing roads in town")
        house_coords: List[Coordinates] = [scene.cm.get_one(Coordinates, entity=house) for house in houses]

        add_town_center(house_coords, scene)
        self.draw_road_across_map(scene)

    def draw_road_across_map(self, scene):
        self._log_info(f"placing highway")
        start = (0, random.randint(2, settings.MAP_WIDTH-3))
        connect_point_to_road_network(scene, start)
        end = (settings.MAP_WIDTH-1, random.randint(2, settings.MAP_HEIGHT-3))
        connect_point_to_road_network(scene, end)
