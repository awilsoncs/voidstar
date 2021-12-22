from abc import ABC, abstractmethod
from dataclasses import dataclass

from engine.component import Component


@dataclass
class MoveListener(Component, ABC):
    @abstractmethod
    def on_move(self, scene):
        pass
