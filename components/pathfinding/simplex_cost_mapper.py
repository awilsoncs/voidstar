import numpy as np
import tcod

import settings
from components import Coordinates
from components.pathfinding.cost_mapper import CostMapper


class SimplexCostMapper(CostMapper):
    def get_cost_map(self, scene):
        noise = tcod.noise.Noise(dimensions=2, algorithm=tcod.noise.Algorithm.SIMPLEX, octaves=3)
        cost = noise[tcod.noise.grid(shape=(settings.MAP_FRAME_WIDTH, settings.MAP_FRAME_HEIGHT), scale=0.5, origin=(0, 0))]
        cost *= 10
        return cost.astype(np.uint16).transpose()
