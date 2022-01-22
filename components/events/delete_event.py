from abc import ABC, abstractmethod
from dataclasses import dataclass

from engine.base_components.events import Event
from engine.base_components.component import Component


@dataclass
class Delete(Event):
    """Add this to an entity to have it delete itself after some time."""
    next_update: int = 0

    def listener_type(self):
        return DeleteListener

    def notify(self, scene, listener):
        if listener.entity == self.entity:
            listener.on_delete(scene)

    def _after_notify(self, scene):
        scene.cm.delete(self.entity)


@dataclass
class DeleteListener(Component, ABC):
    """A world building step."""

    @abstractmethod
    def on_delete(self, scene):
        raise NotImplementedError()
