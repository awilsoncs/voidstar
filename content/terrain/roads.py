from typing import Tuple, List, Iterator

import tcod.path

from components import Entity, Appearance, Coordinates
from components.Sellable import Sellable
from components.pathfinding.road_cost_mapper import RoadCostMapper
from components.pathfinding.simplex_cost_mapper import SimplexCostMapper
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
            RoadMarker(entity=entity_id)
        ]
    )
    return entity


def connect_point_to_road_network(scene, start: Tuple[int, int], trim_start: int = 0):
    road_coords = scene.cm.get(RoadMarker, project=lambda rm: (rm.entity, 100))
    cost_map = RoadCostMapper().get_cost_map(scene)
    best_entity: int = get_new_target(scene, cost_map, start, road_coords)
    best_point: Tuple[int, int] = scene.cm.get_one(Coordinates, entity=best_entity).position
    _draw_road(scene, start, best_point, cost_map, trim_start=trim_start)


def _draw_road(scene, start: Tuple[int, int], end: Tuple[int, int], cost_map, trim_start: int=0):
    for node in _road_between(cost_map, start, end, trim_start=trim_start):
        coords = scene.cm.get(Coordinates, query=lambda c: scene.cm.get_one(RoadMarker, entity=c.entity))
        if coords and coords[0].x == node[0] and coords[0].y == node[1]:
            break
        other_coords = scene.cm.get(Coordinates, query=lambda c: list(c.position) == node, project=lambda c: c.entity)
        for other in other_coords:
            scene.cm.delete(other)
        scene.cm.add(*make_road(node[0], node[1])[1])


def _road_between(
        cost_map,
        start: Tuple[int, int],
        end: Tuple[int, int],
        trim_start: int = 0
) -> Iterator[Tuple[int, int]]:
    graph = tcod.path.SimpleGraph(cost=cost_map, cardinal=2, diagonal=0)
    pf = tcod.path.Pathfinder(graph)
    pf.add_root(start)

    # In the case of houses, need to start one after the normal start point
    path: List[Tuple[int, int]] = pf.path_to(end).tolist()[trim_start:-1]
    for node in path:
        yield node
