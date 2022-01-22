from dataclasses import dataclass

from components.base_components.energy_actor import EnergyActor
from components.weather.weather import Weather
from engine import core


@dataclass
class SnowFall(EnergyActor):
    energy_cost: int = EnergyActor.HALF_HOUR

    def act(self, scene) -> None:
        weather = scene.cm.get_one(Weather, entity=core.get_id("calendar"))
        if not weather:
            return

        if weather.temperature < 5:
            for _ in range(-1 * (weather.temperature - 10)):
                scene.play_window.add_snow()
        else:
            for _ in range(weather.temperature):
                scene.play_window.add_grass()
        self.pass_turn()
