from dataclasses import dataclass
from typing import List

import tcod

from components.base_components.component import Component


@dataclass
class Pathfinder(Component):
    def get_path(self, cost_map, start, end, diagonal=3) -> List[tuple[int, int]]:
        graph = tcod.path.SimpleGraph(cost=cost_map, cardinal=2, diagonal=diagonal)
        pf = tcod.path.Pathfinder(graph)
        pf.add_root(start)
        path = pf.path_to(end).tolist()
        return path
