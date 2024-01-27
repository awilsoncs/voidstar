from abc import ABC, abstractmethod
from dataclasses import dataclass

from engine.components.component import Component
from engine.components.events import Event


@dataclass
class StartGame(Event):
    def listener_type(self):
        return GameStartListener

    def notify(self, scene, listener):
        listener.on_game_start(scene)


class GameStartListener(Component, ABC):
    @abstractmethod
    def on_game_start(self, scene):
        raise NotImplementedError()
