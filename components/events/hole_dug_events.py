from abc import ABC, abstractmethod
from dataclasses import dataclass

from components.base_components.component import Component
from components.base_components.events import Event


@dataclass
class HoleDug(Event):
    def listener_type(self):
        return HoleDugListener

    def notify(self, scene, listener):
        listener.on_hole_dug(scene)


class HoleDugListener(Component, ABC):
    @abstractmethod
    def on_hole_dug(self, scene):
        raise NotImplementedError()
