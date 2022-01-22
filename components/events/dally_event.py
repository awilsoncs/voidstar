from abc import ABC, abstractmethod
from dataclasses import dataclass

from engine.base_components.component import Component
from engine.base_components.events import Event


@dataclass
class DallyEvent(Event):

    def notify(self, scene, listener):
        listener.on_dally(scene)

    def listener_type(self):
        return DallyListener


class DallyListener(Component, ABC):
    """Trigger when the owning entity takes a step."""

    @abstractmethod
    def on_dally(self, scene):
        raise NotImplementedError()