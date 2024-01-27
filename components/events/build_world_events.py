from abc import ABC, abstractmethod
from dataclasses import dataclass

from engine.components.component import Component
from engine.components.events import Event


@dataclass
class BuildWorld(Event):
    """Event to trigger world building steps."""

    def listener_type(self):
        return BuildWorldListener

    def notify(self, scene, listener):
        listener.on_build_world(scene)


@dataclass
class BuildWorldListener(Component, ABC):
    """A world building step."""

    @abstractmethod
    def on_build_world(self, scene):
        raise NotImplementedError()
