from abc import ABC, abstractmethod
from dataclasses import dataclass

from components.base_components.component import Component
from components.base_components.events import Event


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
