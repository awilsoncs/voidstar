import logging
from dataclasses import dataclass

from components import Coordinates
from components.attacks.attack import Attack
from components.attacks.attack_action import AttackAction
from components.structure import Structure
from content.attacks import stab


@dataclass
class SiegeAttack(Attack):
    """Deals heavy damage to structures."""
    damage: int = 1

    def apply_attack(self, scene, target):
        logging.debug(f"EID#{self.entity}::SiegeAttack applying attack against {target}")
        structure = scene.cm.get_one(Structure, entity=target)
        damage = self.damage * 5 if structure else self.damage
        scene.cm.add(AttackAction(entity=self.entity, target=target, damage=damage))
        target_coords = scene.cm.get_one(Coordinates, target)
        scene.cm.add(*stab(self.entity, target_coords.x, target_coords.y)[1])
