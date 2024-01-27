from dataclasses import dataclass
from typing import List

from components import Attributes
from components.attacks.attack_effects.attack_effect import AttackEffect
from engine.components.energy_actor import EnergyActor
from components.events.attack_events import AttackFinished
from components.events.die_events import Die
from engine import constants
from engine.components.entity import Entity


@dataclass
class AttackAction(EnergyActor):
    """Instance of a live attack."""
    target: int = constants.INVALID
    damage: int = 0

    def act(self, scene) -> None:
        this_entity = scene.cm.get_one(Entity, entity=self.entity)
        target_entity = scene.cm.get_one(Entity, entity=self.target)

        scene.warn(f"{this_entity.name} dealt {self.damage} dmg to {target_entity.name}!")

        self._log_info(f"dealing {self.damage} dmg to {self.target}")
        attack_effects: List[AttackEffect] = scene.cm.get_all(AttackEffect, entity=self.entity)
        for attack_effect in attack_effects:
            attack_effect.apply(scene, self.entity, self.target)
        self._handle_entity_damage(scene, self.target, self.damage)

        scene.cm.delete_components(AttackAction)
        scene.cm.add(AttackFinished(entity=self.entity))

    def _handle_entity_damage(self, scene, target, damage):
        target_attributes = scene.cm.get_one(Attributes, entity=target)
        if target_attributes:
            target_attributes.hp -= damage
            target_attributes.hp = max(0, target_attributes.hp)
            if target_attributes.hp <= 0:
                self._log_info(f"applying Die effect")
                scene.cm.add(Die(entity=target_attributes.entity, killer=self.entity))
