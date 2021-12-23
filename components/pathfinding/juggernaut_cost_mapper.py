import numpy as np

import settings
from components.pathfinding.cost_mapper import CostMapper


class StraightLineCostMapper(CostMapper):
    def get_cost_map(self, scene):
        size = (settings.MAP_WIDTH, settings.MAP_HEIGHT)
        cost = np.ones(size, dtype=np.int8, order='F')
        return cost
