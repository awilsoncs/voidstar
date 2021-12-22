from abc import ABC, abstractmethod
from dataclasses import dataclass

from engine.component import Component


@dataclass
class DeleteListener(Component, ABC):
    """A world building step."""

    @abstractmethod
    def on_delete(self, scene):
        raise NotImplementedError()
