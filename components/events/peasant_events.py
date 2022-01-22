from abc import ABC, abstractmethod
from dataclasses import dataclass

from engine.base_components.component import Component
from engine.base_components.events import Event


@dataclass
class PeasantAddedListener(Component, ABC):
    """Respond to peasants moving in."""
    @abstractmethod
    def on_peasant_added(self, scene):
        raise NotImplementedError()


@dataclass
class PeasantAdded(Event):
    """Signal that a new peasant has moved in."""
    def listener_type(self):
        return PeasantAddedListener

    def notify(self, scene, listener):
        listener.on_peasant_added(scene)


@dataclass
class PeasantDiedListener(Component, ABC):
    """Respond to peasant death events."""
    @abstractmethod
    def on_peasant_died(self, scene):
        raise NotImplementedError()


@dataclass
class PeasantDied(Event):
    """Signal that a peasant has died."""
    def listener_type(self):
        return PeasantDiedListener

    def notify(self, scene, listener):
        listener.on_peasant_died(scene)
