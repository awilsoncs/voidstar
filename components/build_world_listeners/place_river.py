import logging
import random

import settings
from components.build_world_listeners.build_world_listeners import BuildWorldListener
from components.pathfinding.pathfinder import Pathfinder
from components.pathfinding.simplex_cost_mapper import SimplexCostMapper
from content.terrain.water import make_water


class PlaceRiver(BuildWorldListener):
    def on_build_world(self, scene):
        logging.info(f"EID#{self.entity}::PlaceRiver placing river")
        cost = SimplexCostMapper().get_cost_map(scene)
        print(cost)
        start = (random.randint(2, settings.MAP_WIDTH-3), 1)
        end = (random.randint(2, settings.MAP_WIDTH-3), settings.MAP_HEIGHT-2)
        river = Pathfinder().get_path(cost, start, end, diagonal=0)
        if not river:
            logging.warning(f"EID#{self.entity}::PlaceRiver could not find a path for river")
        for x, y in river:
            logging.info(f"EID#{self.entity}::PlaceRiver placing water ({x}, {y})")
            scene.cm.add(*make_water(x, y)[1])
