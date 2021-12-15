from abc import ABC, abstractmethod
from dataclasses import dataclass

from engine.component import Component


@dataclass
class BuildWorldListener(Component, ABC):
    """A world building step."""

    @abstractmethod
    def on_build_world(self, scene):
        raise NotImplementedError()
