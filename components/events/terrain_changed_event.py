from abc import ABC, abstractmethod
from dataclasses import dataclass

from engine.components.component import Component
from engine.components.events import Event


@dataclass
class TerrainChangedEvent(Event):

    def listener_type(self):
        return TerrainChangedListener

    def notify(self, scene, listener):
        listener.on_terrain_changed(scene)


class TerrainChangedListener(Component, ABC):

    @abstractmethod
    def on_terrain_changed(self, scene):
        raise NotImplementedError()