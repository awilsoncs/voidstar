from dataclasses import dataclass
from typing import List

from components import Coordinates
from components.actors.energy_actor import EnergyActor
from components.floodable import Floodable
from components.flooder import Flooder
from components.hole_dug_listeners.hole_dug_listener import HoleDugListener
from content.terrain.water import make_water


def _fill_hole(scene, hole):
    coordinates = scene.cm.get_one(Coordinates, entity=hole)
    scene.cm.delete(hole)
    water = make_water(coordinates.x, coordinates.y)
    scene.cm.add(*water[1])


def is_adjacent(scene, first: int, second: int):
    first_coord: Coordinates = scene.cm.get_one(Coordinates, entity=first)
    second_coord: Coordinates = scene.cm.get_one(Coordinates, entity=second)
    return first_coord and second_coord and first_coord.distance_from(second_coord) <= 1


@dataclass
class FloodHolesSystem(EnergyActor, HoleDugListener):
    is_recharging: bool = False

    def on_hole_dug(self, scene, new_hole):
        self.is_recharging = True

    def act(self, scene) -> None:
        # we don't want this running all the time
        self._fill_step(scene)

    def _fill_step(self, scene):
        # find all floodables with an adjacent flooder
        floodables = scene.cm.get(
            Floodable,
            query=lambda this: any(is_adjacent(scene, this.entity, other.entity) for other in scene.cm.get(Flooder)),
            project=lambda this: this.entity
        )

        if not floodables:
            self.is_recharging = False

        for floodable in floodables:
            _fill_hole(scene, floodable)
        self.pass_turn(EnergyActor.HALF_HOUR)



