from abc import ABC, abstractmethod
from dataclasses import dataclass

from components.base_components.events import Event
from components.base_components.component import Component


@dataclass
class DayBegan(Event):
    """Add this to an entity to have it delete itself after some time."""
    day: int = 0

    def listener_type(self):
        return DayBeganListener

    def notify(self, scene, listener):
        listener.on_new_day(scene, self.day)


@dataclass
class DayBeganListener(Component, ABC):
    """A world building step."""

    @abstractmethod
    def on_new_day(self, scene, day):
        raise NotImplementedError()
