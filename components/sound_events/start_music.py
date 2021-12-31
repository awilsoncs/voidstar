from dataclasses import dataclass

from components.game_start_listeners.game_start_listener import GameStartListener
from components.season_reset_listeners.seasonal_actor import SeasonResetListener


@dataclass
class StartMusic(GameStartListener, SeasonResetListener):
    def on_season_reset(self, scene):
        scene.sound.play('town')

    def on_game_start(self, scene):
        scene.sound.play('town')
