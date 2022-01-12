from dataclasses import dataclass
import random

from components.actors.energy_actor import EnergyActor
from components.events.new_day_event import DayBeganListener
from components.events.start_game_events import GameStartListener
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from components.world_building.world_parameters import WorldParameters
from engine import core


@dataclass
class Weather(DayBeganListener, GameStartListener, SeasonResetListener):
    temperature: int = 20
    seasonal_norm: int = 20
    energy_cost: int = EnergyActor.DAILY

    def on_new_day(self, scene, day):
        self.set_temperature()

    def on_game_start(self, scene):
        self.set_seasonal_norm(scene, "Spring")

    def on_season_reset(self, scene, season):
        self.set_seasonal_norm(scene, season)

    def set_seasonal_norm(self, scene, season):
        seasonal_temps = {
            "Spring": 20,
            "Summer": 30,
            "Fall": 10,
            "Winter": -5
        }
        self.seasonal_norm = seasonal_temps[season]
        world_params = scene.cm.get_one(WorldParameters, entity=core.get_id("world"))
        self.seasonal_norm += world_params.temperature_modifier
        self._log_info(f"set normal temp {self.seasonal_norm}")
        old_temp = self.temperature
        self.set_temperature()

        if old_temp > 0 > self.temperature:
            scene.message("It is freezing outside.")
        elif old_temp < 0 < self.temperature:
            scene.message("The weather warmed up.")

    def set_temperature(self):
        self.temperature = self.seasonal_norm + random.randint(-10, 10)
        self._log_info(f"set daily temp {self.temperature}")
