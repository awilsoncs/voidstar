from dataclasses import dataclass

from components.actors.energy_actor import EnergyActor
from components.season_reset_listeners.seasonal_actor import SeasonResetListener


@dataclass
class SnowFall(EnergyActor, SeasonResetListener):
    energy_cost: int = EnergyActor.HALF_HOUR
    is_recharging: bool = False
    energy: int = -1 * EnergyActor.HALF_HOUR

    def on_season_reset(self, scene, season):
        if season == 'Winter':
            scene.message("Snow begins to fall.")
            self.is_recharging = True
        else:
            self.is_recharging = False

    def act(self, scene) -> None:
        for _ in range(10):
            scene.play_window.add_snow()
        self.pass_turn()
