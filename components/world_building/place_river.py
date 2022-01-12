import random

import settings
from components.events.build_world_events import BuildWorldListener
from components.pathfinding.pathfinder import Pathfinder
from components.pathfinding.simplex_cost_mapper import SimplexCostMapper
from components.world_building.world_parameters import WorldParameters
from content.terrain.water import make_water
from engine import core


class PlaceRiver(BuildWorldListener):
    def on_build_world(self, scene):
        self._log_info(f"placing river")
        cost = SimplexCostMapper().get_cost_map(scene)
        print(cost)
        start = (random.randint(2, settings.MAP_WIDTH-3), 0)
        end = (random.randint(2, settings.MAP_WIDTH-3), settings.MAP_HEIGHT-1)
        river = Pathfinder().get_path(cost, start, end, diagonal=0)
        if not river:
            self._log_warning(f"could not find a path for river")
        for x, y in river:
            self._log_debug(f"placing water ({x}, {y})")
            params = scene.cm.get_one(WorldParameters, entity=core.get_id("world"))
            scene.cm.add(*make_water(x, y, rapidness=params.river_rapids)[1])
