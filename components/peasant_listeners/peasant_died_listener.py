from abc import ABC, abstractmethod

from engine.component import Component


class PeasantDiedListener(Component, ABC):

    @abstractmethod
    def on_peasant_died(self, scene):
        raise NotImplementedError()
