from abc import ABC, abstractmethod
from dataclasses import dataclass

from components.events.events import Event
from engine.component import Component


@dataclass
class HoleDug(Event):
    def listener_type(self):
        return HoleDugListener

    def notify(self, scene, listener):
        listener.on_hole_dug(scene, self.entity)


class HoleDugListener(Component, ABC):
    @abstractmethod
    def on_hole_dug(self, scene):
        raise NotImplementedError()
