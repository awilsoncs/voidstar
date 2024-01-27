from abc import ABC, abstractmethod
from dataclasses import dataclass

from engine.components.component import Component


@dataclass
class TargetEvaluator(Component, ABC):
    @abstractmethod
    def get_targets(self, scene):
        pass
