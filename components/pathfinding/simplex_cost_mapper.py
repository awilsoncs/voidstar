import numpy as np
import tcod

import settings
from components.pathfinding.cost_mapper import CostMapper


class SimplexCostMapper(CostMapper):
    def get_cost_map(self, scene):
        noise = tcod.noise.Noise(dimensions=2, algorithm=tcod.noise.Algorithm.SIMPLEX, octaves=10)
        cost = noise[tcod.noise.grid(shape=(settings.MAP_WIDTH-2, settings.MAP_HEIGHT-2), scale=0.1, origin=(0, 0))]

        border = np.zeros((settings.MAP_WIDTH, settings.MAP_HEIGHT), order='F', dtype=float)
        border[1:settings.MAP_WIDTH-1, 1:settings.MAP_HEIGHT-1] = cost.transpose()

        border += 1
        border *= 1000
        border = border.astype(np.uint8)
        return border
