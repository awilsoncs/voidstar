import numpy as np
import tcod

import settings
from components import Coordinates


def get_new_target(scene, cost_map, start, entity_values) -> int:
    dist = tcod.path.maxarray((settings.MAP_WIDTH, settings.MAP_HEIGHT), dtype=np.int32)
    dist[start[0], start[1]] = 0
    tcod.path.dijkstra2d(dist, cost_map, 2, 3, out=dist)
    # find the cost of all the possible targets
    best = (None, 0)
    for entity, value in entity_values:
        target_coords = scene.cm.get_one(Coordinates, entity=entity)
        cost_to_reach = float(dist[target_coords.x, target_coords.y]) ** 2
        value = float(value) / cost_to_reach
        if value > best[1]:
            best = (entity, value)

    return best[0]
