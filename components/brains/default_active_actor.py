import logging
from dataclasses import dataclass
from typing import Optional

from components import Coordinates, Entity
from components.actions.attack_action import AttackAction
from components.animation_effects.blinker import AnimationBlinker
from components.attacks.attack import Attack
from components.brains.brain import Brain
from components.brains.sleeping_brain import SleepingBrain
from components.death_listeners.die import Die
from components.edible import Edible
from components.pathfinding.breadcrumb_tracker import BreadcrumbTracker
from components.pathfinding.cost_mapper import CostMapper
from components.pathfinding.normal_cost_mapper import NormalCostMapper
from components.pathfinding.pathfinder import Pathfinder
from components.pathfinding.target_evaluation.hordeling_target_evaluator import HordelingTargetEvaluator
from components.pathfinding.target_evaluation.target_evaluator import TargetEvaluator
from components.pathfinding.target_selection import get_new_target
from content.attacks import stab
from engine import constants, palettes
from engine.core import log_debug
from components.actors import VECTOR_STEP_MAP


@dataclass
class DefaultActiveActor(Brain):
    target: int = constants.INVALID
    cost_map = None

    @log_debug(__name__)
    def act(self, scene):
        self.cost_map = self.get_cost_map(scene)

        target_evaluator = scene.cm.get_one(TargetEvaluator, entity=self.entity)
        if not target_evaluator:
            logging.warning(f"EID#{self.entity}::DefaultActiveActor missing target evaluator")
            target_evaluator = HordelingTargetEvaluator()

        entity_values = target_evaluator.get_targets(scene)

        if not entity_values:
            # No targets
            self.pass_turn()
            return

        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        self.target = get_new_target(scene, self.cost_map, (coords.x, coords.y), entity_values)

        if self.is_target_in_range(scene):
            if self.should_eat(scene):
                self.eat_target(scene)
            else:
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
        logging.debug(f"EID#{self.entity}::DefaultActiveActor stepping towards target {self.target}")
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        next_step_node = self.get_next_step(scene)
        next_step = (next_step_node[0] - coords.x, next_step_node[1] - coords.y)
        self.intention = VECTOR_STEP_MAP[next_step]

    def should_eat(self, scene):
        logging.debug(f"EID#{self.entity}::DefaultActiveActor checking for edibility of {self.target}")
        edible = scene.cm.get_one(Edible, entity=self.target)
        return edible is not None

    def eat_target(self, scene):
        logging.debug(f"EID#{self.entity}::DefaultActiveActor eating target {self.target}")
        scene.cm.add(Die(entity=self.target))

        this_entity = scene.cm.get_one(Entity, entity=self.entity)
        target_entity = scene.cm.get_one(Entity, entity=self.target)
        scene.warn(f"{this_entity.name} ate a {target_entity.name}!")
        edible = scene.cm.get_one(Edible, entity=self.target)

        self.sleep(scene, edible.sleep_for)
        self.pass_turn()

    def attack_target(self, scene):
        logging.debug(f"EID#{self.entity}::DefaultActiveActor attacking target {self.target}")

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
            logging.warning(f"EID#{self.entity}::DefaultActiveActor found no valid path")
            return None

    def sleep(self, scene, sleep_for):
        logging.debug(f"EID#{self.entity}::DefaultActiveActor falling asleep")
        new_controller = SleepingBrain(entity=self.entity, old_actor=self.id, turns=sleep_for)
        blinker = AnimationBlinker(
            entity=self.entity,
            new_symbol='z',
            new_color=palettes.LIGHT_WATER,
            timer_delay=500
        )
        scene.cm.stash_component(self.id)
        scene.cm.add(new_controller, blinker)
