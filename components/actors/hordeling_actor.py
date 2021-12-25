from dataclasses import dataclass
from typing import Optional

from components import Coordinates
from components.attacks.attack_action import AttackAction
from components.actors.energy_actor import EnergyActor
from components.attacks.attack import Attack
from components.pathfinding.breadcrumb_tracker import BreadcrumbTracker
from components.pathfinding.cost_mapper import CostMapper
from components.pathfinding.normal_cost_mapper import NormalCostMapper
from components.pathfinding.pathfinder import Pathfinder
from components.pathfinding.target_selection import get_new_target
from components.target_value import TargetValue
from content.attacks import stab
from engine import constants
from engine.core import log_debug
from components.actors import VECTOR_STEP_MAP
from systems.utilities import set_intention


@dataclass
class HordelingActor(EnergyActor):
    target: int = constants.INVALID
    cost_map = None

    @log_debug(__name__)
    def act(self, scene):
        self.cost_map = self.get_cost_map(scene)

        entity_values = [(tv.entity, tv.value) for tv in scene.cm.get(TargetValue)]

        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        self.target = get_new_target(scene, self.cost_map, (coords.x, coords.y), entity_values)

        if self.is_target_in_range(scene):
            self.attack_target(scene)
        else:
            self.move_towards_target(scene)

    def get_cost_map(self, scene):
        cost_mapper: Optional[CostMapper] = scene.cm.get_one(CostMapper, entity=self.entity)
        if cost_mapper:
            return cost_mapper.get_cost_map(scene)
        else:
            # If one hasn't been set up, we default to the normal behavior
            return NormalCostMapper(entity=self.entity).get_cost_map(scene)

    def move_towards_target(self, scene):
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        next_step_node = self.get_next_step(scene)
        next_step = (next_step_node[0] - coords.x, next_step_node[1] - coords.y)
        step_intention = VECTOR_STEP_MAP[next_step]
        set_intention(scene, self.entity, 0, step_intention)

    def attack_target(self, scene):
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        target = scene.cm.get_one(Coordinates, entity=self.target)
        facing = coords.direction_towards(target)
        attack = scene.cm.get_one(Attack, entity=self.entity)
        scene.cm.add(
            AttackAction(
                entity=self.entity,
                target=self.target,
                damage=attack.damage
            )
        )
        scene.cm.add(
            *stab(
                self.entity,
                coords.x + facing[0],
                coords.y + facing[1]
            )[1]
        )
        self.pass_turn()

    def is_target_in_range(self, scene) -> bool:
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        target = scene.cm.get_one(Coordinates, entity=self.target)
        return coords.distance_from(target) < 2

    def get_next_step(self, scene):
        self_coords = scene.cm.get_one(Coordinates, entity=self.entity)
        target_coords = scene.cm.get_one(Coordinates, entity=self.target)
        path = Pathfinder().get_path(self.cost_map, self_coords.position, target_coords.position)

        breadcrumb_tracker = scene.cm.get_one(BreadcrumbTracker, entity=self.entity)
        if breadcrumb_tracker:
            breadcrumb_tracker.add_breadcrumbs(scene, path)

        path = [p for p in path]

        if path:
            return path[1]
        else:
            return None


