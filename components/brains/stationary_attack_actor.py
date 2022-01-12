from dataclasses import dataclass

from components import Coordinates
from components.actions.attack_action import AttackAction
from components.attacks.attack import Attack
from components.brains.brain import Brain
from components.events.attack_started_events import AttackStartListener
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from components.tags.hordeling_tag import HordelingTag
from content.attacks import stab
from engine import constants
from engine.core import log_debug


@dataclass
class StationaryAttackActor(Brain, SeasonResetListener, AttackStartListener):
    """Stand in place and attack any enemy in range."""
    target: int = constants.INVALID
    cost_map = None
    root_x: int = constants.INVALID
    root_y: int = constants.INVALID

    def on_season_reset(self, scene, season):
        self.teleport_to_root(scene)

    def on_attack_start(self, scene):
        self.teleport_to_root(scene)

    def teleport_to_root(self, scene):
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        coords.x = self.root_x
        coords.y = self.root_y

    @log_debug(__name__)
    def act(self, scene):
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        targets = scene.cm.get(
            Coordinates,
            query=lambda c: scene.cm.get_one(HordelingTag, entity=c.entity) and c.distance_from(coords) <= 2,
            project=lambda c: c.entity
        )
        if not targets:
            self.pass_turn()
            return
        self.target = targets.pop()
        self.attack_target(scene)

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
