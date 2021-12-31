import random
from dataclasses import dataclass

from components.actors.energy_actor import EnergyActor
from components.season_reset_listeners.seasonal_actor import SeasonResetListener


@dataclass
class SnowFall(EnergyActor, SeasonResetListener):
    energy_cost: int = EnergyActor.HALF_HOUR
    temperature: int = 10

    def on_season_reset(self, scene, season):
        if season == 'Winter':
            scene.message("Snow begins to fall.")
            self.temperature = -10
        elif season == 'Spring':
            self.temperature = random.randint(-2, 10)
        elif season == 'Summer':
            self.temperature = 20
        elif season == 'Fall':
            self.temperature = random.randint(-5, 5)
        else:
            raise ValueError(f"EID#{self.entity}::SnowFall.on_season_reset received bad season: {season}")

    def act(self, scene) -> None:
        if self.temperature < 0:
            for _ in range(self.temperature * -1):
                scene.play_window.add_snow()
        else:
            for _ in range(self.temperature):
                scene.play_window.add_grass()
        self.pass_turn()
