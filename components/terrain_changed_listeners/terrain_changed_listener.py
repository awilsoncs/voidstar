from abc import ABC, abstractmethod

from engine.components.component import Component


class TerrainChangedListener(Component, ABC):

    @abstractmethod
    def on_terrain_changed(self, scene):
        raise NotImplementedError()
