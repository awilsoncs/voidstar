import numpy as np
import tcod

import settings
from components import Coordinates
from components.pathfinding.cost_mapper import CostMapper


class SimplexCostMapper(CostMapper):
    def get_cost_map(self, scene):
        noise = tcod.noise.Noise(dimensions=2, algorithm=tcod.noise.Algorithm.SIMPLEX, octaves=1)
        cost = noise[tcod.noise.grid(shape=(settings.MAP_WIDTH-6, settings.MAP_HEIGHT-6), scale=0.1, origin=(0, 0))]

        # Block paths from going into the map border trees
        blocked_area = np.ones((settings.MAP_WIDTH, settings.MAP_HEIGHT), order='F', dtype=float) * 1000

        # Want a high cost frame around the village so that hordelings don't get trapped behind impassible terrain
        avoid_area = np.ones((settings.MAP_WIDTH-2, settings.MAP_HEIGHT-2), order='F', dtype=float) * 2
        blocked_area[1:settings.MAP_WIDTH-1, 1:settings.MAP_HEIGHT-1] = avoid_area
        blocked_area[3:settings.MAP_WIDTH-3, 3:settings.MAP_HEIGHT-3] = cost.transpose()
        blocked_area[1:settings.MAP_WIDTH-1, 1:settings.MAP_HEIGHT-1] += 1
        blocked_area[1:settings.MAP_WIDTH-1, 1:settings.MAP_HEIGHT-1] *= 1000
        blocked_area = blocked_area.astype(np.uint16)
        return blocked_area
