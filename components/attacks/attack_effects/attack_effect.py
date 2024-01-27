from abc import abstractmethod, ABC
from dataclasses import dataclass

from engine.components.component import Component


@dataclass
class AttackEffect(Component, ABC):

    @abstractmethod
    def apply(self, scene, source, target):
        raise NotImplementedError("Attack effect apply must be implemented.")
