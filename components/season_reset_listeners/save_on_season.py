import logging
from dataclasses import dataclass

import settings
from components.game_start_listeners.game_start_listener import GameStartListener
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from components.serialization.save_game import SaveGame


@dataclass
class SaveOnSeasonReset(SeasonResetListener, GameStartListener):
    """Save the game each season."""

    def on_game_start(self, scene):
        self.autosave(scene)

    def on_season_reset(self, scene, season):
        self.autosave(scene)

    def autosave(self, scene):
        if not settings.AUTOSAVE:
            self._log_info(f"autosave is disabled")
            return
        scene.cm.add(SaveGame(entity=scene.player))
