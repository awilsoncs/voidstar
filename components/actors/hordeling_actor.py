import logging
import random
from dataclasses import dataclass
from typing import Tuple, List

import numpy as np
import tcod

import settings
from components import Coordinates
from components.actions.attack_action import AttackAction
from components.actors.energy_actor import EnergyActor
from components.attack import Attack
from components.target_value import TargetValue
from content.attacks import stab
from content.pathfinder_cost import PathfinderCost
from engine import constants
from engine.core import log_debug
from components.actors import VECTOR_STEP_MAP, STEPS
from systems.utilities import set_intention


def get_cost_map(scene):
    size = (settings.MAP_WIDTH, settings.MAP_HEIGHT)
    cost = np.ones(size, dtype=np.int8, order='F')
    for cost_component in scene.cm.get(PathfinderCost):
        coords = scene.cm.get_one(Coordinates, entity=cost_component.entity)
        cost[coords.x, coords.y] += cost_component.cost
    return cost


@dataclass
class HordelingActor(EnergyActor):
    target: int = constants.INVALID
    cost_map = None

    @log_debug(__name__)
    def act(self, scene):
        self.cost_map = get_cost_map(scene)

        if self.target not in scene.cm.entities:
            self.target = self.get_new_target(scene)

        if self.is_target_in_range(scene):
            self.attack_target(scene)
        else:
            self.move_towards_target(scene)

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
                recipient=self.target,
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

    def is_target_in_range(self, scene) -> bool:
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        target = scene.cm.get_one(Coordinates, entity=self.target)
        return coords.distance_from(target) < 2

    def get_next_step(self, scene):
        graph = tcod.path.SimpleGraph(cost=self.cost_map, cardinal=2, diagonal=3)
        pf = tcod.path.Pathfinder(graph)

        self_coords = scene.cm.get_one(Coordinates, entity=self.entity)
        pf.add_root((self_coords.x, self_coords.y))

        target_coords = scene.cm.get_one(Coordinates, entity=self.target)
        path: List[Tuple[int, int]] = pf.path_to((target_coords.x, target_coords.y))[1:].tolist()
        if path:
            return path[0]
        else:
            return None

    def get_new_target(self, scene) -> int:
        logging.debug(f"EID#{self.entity}::HordelingActor hunting new target")
        dist = tcod.path.maxarray((settings.MAP_WIDTH, settings.MAP_HEIGHT), dtype=np.int32)
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        dist[coords.x, coords.y] = 0
        tcod.path.dijkstra2d(dist, self.cost_map, 2, 3, out=dist)
        # find the cost of all the possible targets
        best = (None, 0)
        for target in scene.cm.get(TargetValue):
            target_coords = scene.cm.get_one(Coordinates, entity=target.entity)
            cost_to_reach = float(dist[target_coords.x, target_coords.y])
            value = float(target.value) / cost_to_reach
            if value > best[1]:
                logging.debug(f"Found better target: {target.entity} at value {value}")
                best = (target.entity, value)

        return best[0]
