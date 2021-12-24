import logging
import random
from collections import Iterator
from typing import Tuple, List

import tcod.los

from components import Coordinates
from components.build_world_listeners.build_world_listeners import BuildWorldListener
from components.house_structure import HouseStructure
from components.pathfinding.road_cost_mapper import RoadCostMapper
from components.tags.town_center_flag import TownCenterFlag
from content.terrain.roads import make_road
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


def road_between(cost_map, start, end) -> Iterator[Tuple[int, int]]:
    graph = tcod.path.SimpleGraph(cost=cost_map, cardinal=2, diagonal=100)
    pf = tcod.path.Pathfinder(graph)
    pf.add_root(start)
    path: List[Tuple[int, int]] = pf.path_to(end).tolist()[2:-2]
    for node in path:
        yield node


class PlaceRoads(BuildWorldListener):
    def on_build_world(self, scene):
        logging.info(f"EID#{self.entity}::PlaceRoads placing roads in town")
        houses = scene.cm.get(HouseStructure, project=lambda hs: hs.house_id)
        house_coords = [scene.cm.get_one(Coordinates, entity=house) for house in houses]

        # Identify the town center by averaging the coords
        avg_x, avg_y = get_town_center(house_coords, scene)

        for coord in list(get_3_by_3_box(avg_x, avg_y)):
            scene.cm.add(*make_road(coord[0], coord[1])[1])

        town_center = make_road(avg_x, avg_y)
        town_center[1].append(TownCenterFlag(entity=town_center[0]))
        scene.cm.add(*town_center[1])

        # Draw roads component-wise to the town center
        cost_map = RoadCostMapper().get_cost_map(scene)

        for coord in house_coords:
            logging.info(f"EID#{self.entity}::PlaceRoads ({coord.x}, {coord.y}) to ({avg_x}, {avg_y})")

            for node in road_between(cost_map, (coord.x, coord.y), (avg_x, avg_y)):
                if scene.cm.get(Coordinates, query=lambda c: c.x == node[0] and c.y == node[1]):
                    break
                scene.cm.add(*make_road(node[0], node[1])[1])
