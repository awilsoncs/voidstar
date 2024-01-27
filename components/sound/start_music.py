from dataclasses import dataclass

from components.events.start_game_events import GameStartListener


@dataclass
class StartMusic(GameStartListener):

    def on_game_start(self, scene):
        scene.sound.play('town')
