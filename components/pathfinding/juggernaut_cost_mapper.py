import logging

import numpy as np

import settings
from components import Coordinates, Attributes, Entity
from components.material import Material
from components.pathfinding.cost_mapper import CostMapper


class StraightLineCostMapper(CostMapper):
    def get_cost_map(self, scene):
        size = (settings.MAP_WIDTH, settings.MAP_HEIGHT)
        cost = np.ones(size, dtype=np.int8, order='F')

        points = scene.cm.get(Coordinates)
        for point in points:
            material = scene.cm.get_one(Material, entity=point.entity)
            attributes = scene.cm.get_one(Attributes, entity=point.entity)
            if material and material.blocks and not attributes:
                # You can't bash your way through this one
                entity = scene.cm.get_one(Entity, entity=point.entity)
                logging.debug(
                    f"EID#{self.entity}::StraightLineCostMapper found impassible terrain: "
                    f"{entity.name} at position {point.position}"
                )
                cost[point.x, point.y] = 0
        return cost
