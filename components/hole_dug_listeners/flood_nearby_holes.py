from dataclasses import dataclass
from typing import List

from components import Coordinates
from components.floodable import Floodable
from components.fluid import Fluid
from components.hole_dug_listeners.hole_dug_listener import HoleDugListener
from content.terrain.water import make_water


def _fill_hole(scene, hole):
    coordinates = scene.cm.get_one(Coordinates, entity=hole)
    scene.cm.delete(hole)
    water = make_water(coordinates.x, coordinates.y)
    scene.cm.add(*water[1])
    return water[0]


def is_adjacent(scene, first: int, second: int):
    first_coord: Coordinates = scene.cm.get_one(Coordinates, entity=first)
    second_coord: Coordinates = scene.cm.get_one(Coordinates, entity=second)
    return first_coord and second_coord and first_coord.distance_from(second_coord) <= 1


def _has_adjacent_fluid(scene, hole: int):
    fluids: List[int] = scene.cm.get(
        Fluid,
        query=lambda f: is_adjacent(scene, hole, f.entity),
        project=lambda f: f.entity
    )
    return bool(fluids)


def _get_neighboring_holes(scene, water: int) -> List[int]:
    return scene.cm.get(
        Floodable,
        query=lambda f: is_adjacent(scene, f.entity, water),
        project=lambda f: f.entity
    )


def _fill_from(scene, start_hole):
    remaining_holes = [start_hole]

    while remaining_holes:
        next_hole = remaining_holes.pop()
        new_water = _fill_hole(scene, next_hole)

        new_neighbors: List[int] = [
            hole
            for hole in _get_neighboring_holes(scene, new_water)
        ]

        remaining_holes += new_neighbors


@dataclass
class FloodHoles(HoleDugListener):
    def on_hole_dug(self, scene, new_hole):
        if not _has_adjacent_fluid(scene, new_hole):
            return

        _fill_from(scene, new_hole)

