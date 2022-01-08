import logging
from dataclasses import dataclass
import random

from components.actors.energy_actor import EnergyActor
from components.build_world_listeners.world_parameters import WorldParameters
from components.game_start_listeners.game_start_listener import GameStartListener
from components.season_reset_listeners.seasonal_actor import SeasonResetListener


@dataclass
class Weather(EnergyActor, GameStartListener, SeasonResetListener):
    temperature: int = 20
    seasonal_norm: int = 20
    energy_cost: int = EnergyActor.DAILY

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
        world_params = scene.cm.get_one(WorldParameters, entity=scene.player)
        self.seasonal_norm += world_params.temperature_modifier
        logging.info(f"EID#{self.entity}::Weather.on_season_reset set normal temp {self.seasonal_norm}")
        self.set_temperature()

    def set_temperature(self):
        self.temperature = self.seasonal_norm + random.randint(-10, 10)
        logging.info(f"EID#{self.entity}::Weather.act set daily temp {self.temperature}")

    def act(self, scene):
        self.set_temperature()
        self.pass_turn()
