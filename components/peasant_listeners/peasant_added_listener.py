from abc import ABC, abstractmethod

from engine.components.component import Component


class PeasantAddedListener(Component, ABC):

    @abstractmethod
    def on_peasant_added(self, scene):
        raise NotImplementedError()
