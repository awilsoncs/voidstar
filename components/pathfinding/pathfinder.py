from collections import Generator
from dataclasses import dataclass

import tcod

from engine.component import Component


@dataclass
class Pathfinder(Component):
    def get_path(self, cost_map, start, end, diagonal=3) -> Generator[tuple[int, int]]:
        graph = tcod.path.SimpleGraph(cost=cost_map, cardinal=2, diagonal=diagonal)
        pf = tcod.path.Pathfinder(graph)
        pf.add_root(start)
        path = pf.path_to(end).tolist()
        for node in path:
            yield node
