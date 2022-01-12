from dataclasses import dataclass

from components.events.events import Event
from components.game_start_listeners.game_start_listener import GameStartListener


@dataclass
class StartGame(Event):
    def listener_type(self):
        return GameStartListener

    def notify(self, scene, listener):
        listener.on_game_start(scene)
