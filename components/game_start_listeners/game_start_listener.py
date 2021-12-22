from abc import ABC, abstractmethod

from engine.component import Component


class GameStartListener(Component, ABC):

    @abstractmethod
    def on_game_start(self, scene):
        raise NotImplementedError()
