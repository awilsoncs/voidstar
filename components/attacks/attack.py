from abc import ABC, abstractmethod
from dataclasses import dataclass

from engine.component import Component


@dataclass
class Attack(Component, ABC):
    damage: int = 1

    @abstractmethod
    def apply_attack(self, scene, target):
        raise NotImplementedError("Attack must use subclass")
