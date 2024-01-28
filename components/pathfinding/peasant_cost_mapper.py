import numpy as np

import settings
from components import Coordinates
from components.movement.drain_on_enter import DrainOnEnter
from components.pathfinding.cost_mapper import CostMapper
from components.pathfinder_cost import PathfinderCost


class PeasantCostMapper(CostMapper):
    """Apply an additional cost to anything that might be painful to step on."""
    def get_cost_map(self, scene):
        size = (settings.MAP_FRAME_WIDTH, settings.MAP_FRAME_HEIGHT)
        cost = np.ones(size, dtype=np.int8, order='F')
        for cost_component in scene.cm.get(PathfinderCost):
            coords = scene.cm.get_one(Coordinates, entity=cost_component.entity)
            cost[coords.x, coords.y] = cost_component.cost

        for drain_on_enter in scene.cm.get(DrainOnEnter):
            coords = scene.cm.get_one(Coordinates, entity=drain_on_enter.entity)
            cost[coords.x, coords.y] += drain_on_enter.damage * 20

        return cost
