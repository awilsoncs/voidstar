from abc import ABC, abstractmethod

from engine.component import Component


class HoleDugListener(Component, ABC):

    @abstractmethod
    def on_hole_dug(self, scene, new_hole):
        raise NotImplementedError()
