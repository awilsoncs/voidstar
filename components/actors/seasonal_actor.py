from abc import ABC, abstractmethod

from engine.component import Component


class SeasonalActor(Component, ABC):

    @abstractmethod
    def act(self, scene):
        raise NotImplementedError()
