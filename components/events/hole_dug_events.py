from abc import ABC, abstractmethod
from dataclasses import dataclass

from engine.components.events import Event
from engine.components.component import Component


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
