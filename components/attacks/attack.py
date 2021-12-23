from dataclasses import dataclass

from components import Coordinates
from components.attacks.attack_action import AttackAction
from content.attacks import stab
from engine.component import Component


@dataclass
class Attack(Component):
    damage: int = 1

    def apply_attack(self, scene, target):
        scene.cm.add(AttackAction(entity=self.entity, target=target, damage=1))
        target_coords = scene.cm.get_one(Coordinates, target)
        scene.cm.add(*stab(self.entity, target_coords.x, target_coords.y)[1])
