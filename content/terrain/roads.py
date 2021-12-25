from typing import Tuple, List, Iterator

import tcod.path

from components import Entity, Appearance, Coordinates
from components.pathfinding.road_cost_mapper import RoadCostMapper
from components.pathfinding.target_selection import get_new_target
from components.states.move_cost_affectors import EasyTerrain
from components.tags.road_marker import RoadMarker
from engine import core, palettes
from engine.component import Component
from engine.constants import PRIORITY_LOWEST


def make_road(x, y):
    entity_id = core.get_id()
    entity: Tuple[int, List[Component]] = (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='road', static=True),
            Appearance(entity=entity_id, symbol='.', color=palettes.GOLD, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOWEST),
            EasyTerrain(entity=entity_id),
            RoadMarker(entity=entity_id),
        ]
    )
    return entity


def connect_point_to_road_network(scene, start: Tuple[int, int]):
    road_coords = scene.cm.get(RoadMarker, project=lambda rm: (rm.entity, 100))
    cost_map = RoadCostMapper().get_cost_map(scene)
    best_entity: int = get_new_target(scene, cost_map, start, road_coords)
    best_point: Tuple[int, int] = scene.cm.get_one(Coordinates, entity=best_entity).position
    _draw_road(scene, start, best_point, cost_map)


def _draw_road(scene, start: Tuple[int, int], end: Tuple[int, int], cost_map):
    for node in _road_between(cost_map, start, end):
        if scene.cm.get(Coordinates, query=lambda c: c.x == node[0] and c.y == node[1]):
            break
        scene.cm.add(*make_road(node[0], node[1])[1])


def _road_between(cost_map, start: Tuple[int, int], end: Tuple[int, int]) -> Iterator[Tuple[int, int]]:
    graph = tcod.path.SimpleGraph(cost=cost_map, cardinal=2, diagonal=5)
    pf = tcod.path.Pathfinder(graph)
    pf.add_root(start)
    path: List[Tuple[int, int]] = pf.path_to(end).tolist()[2:-1]
    for node in path:
        yield node
