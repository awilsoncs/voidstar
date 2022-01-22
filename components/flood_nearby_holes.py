from dataclasses import dataclass

from components import Coordinates
from components.base_components.energy_actor import EnergyActor
from components.floodable import Floodable
from components.flooder import Flooder
from components.events.hole_dug_events import HoleDugListener
from components.tags.water_tag import WaterTag
from components.world_building.world_parameters import WorldParameters
from content.terrain.water import make_water, make_swampy_water
from engine import core


def _fill_hole(scene, hole, painter):
    world_params = scene.cm.get_one(WorldParameters, entity=core.get_id("world"))

    coordinates = scene.cm.get_one(Coordinates, entity=hole)
    scene.cm.delete(hole)
    water = painter(coordinates.x, coordinates.y, rapidness=world_params.river_rapids)
    scene.cm.add(*water[1])


def is_adjacent(scene, first: int, second: int):
    first_coord: Coordinates = scene.cm.get_one(Coordinates, entity=first)
    second_coord: Coordinates = scene.cm.get_one(Coordinates, entity=second)
    return first_coord and second_coord and first_coord.distance_from(second_coord) <= 1


@dataclass
class FloodHolesSystem(EnergyActor, HoleDugListener):
    is_recharging: bool = False

    def on_hole_dug(self, scene):
        self._log_debug("beginning to fill nearby holes")
        self.is_recharging = True

    def act(self, scene) -> None:
        self._fill_step(scene)

    def _fill_step(self, scene):
        # find all floodables with an adjacent flooder
        floodables = scene.cm.get(Floodable)
        flooders = scene.cm.get(Flooder)

        found = False
        self._log_debug("attempting to fill")
        for floodable in floodables:
            nearby_flooders = [
                flooder
                for flooder in flooders
                if is_adjacent(scene, floodable.entity, flooder.entity)
            ]

            if nearby_flooders:
                found = True
                if any(scene.cm.get_one(WaterTag, entity=flooder.entity).is_dirty for flooder in nearby_flooders):
                    _fill_hole(scene, floodable.entity, make_swampy_water)
                else:
                    _fill_hole(scene, floodable.entity, make_water)

        if not found:
            self.is_recharging = False
            self._log_debug("done filling available floodables")

        self.pass_turn(EnergyActor.HALF_HOUR)



