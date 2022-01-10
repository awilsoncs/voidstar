from dataclasses import dataclass

from components.game_start_listeners.game_start_listener import GameStartListener
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from components.serialization.save_game import SaveGame


@dataclass
class SaveOnSeasonReset(SeasonResetListener, GameStartListener):
    """Save the game each season."""

    def on_game_start(self, scene):
        scene.cm.add(SaveGame(entity=scene.player))

    def on_season_reset(self, scene, season):
        scene.cm.add(SaveGame(entity=scene.player))
