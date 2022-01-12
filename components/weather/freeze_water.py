import logging
import random
from dataclasses import dataclass

from components.actors.energy_actor import EnergyActor
from components.events.attack_started_events import AttackStartListener
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from components.tags.ice_tag import IceTag
from components.tags.water_tag import WaterTag
from components.weather.weather import Weather
from content.terrain.water import freeze, thaw
from engine import core


@dataclass
class FreezeWater(EnergyActor, AttackStartListener, SeasonResetListener):
    energy_cost: int = EnergyActor.HALF_HOUR

    def on_attack_start(self, scene):
        logging.debug(f"EID#{self.entity}::FreezeWater pausing freezing")
        self.is_recharging = False

    def on_season_reset(self, scene, season):
        logging.debug(f"EID#{self.entity}::FreezeWater unpausing freezing")
        self.is_recharging = True

    def act(self, scene) -> None:
        weather = scene.cm.get_one(Weather, entity=core.get_id("calendar"))

        if not weather:
            return

        if weather.temperature < 0:
            self.freeze_n(scene, max(weather.temperature * -1, 5))
        else:
            self.thaw_n(scene, max(weather.temperature, 5))
        self.pass_turn()

    def freeze_n(self, scene, n):
        logging.debug(f"EID#{self.entity}::FreezeWater freezing {n}")
        waters = scene.cm.get(WaterTag, project=lambda wt: wt.entity)
        if not waters:
            return

        n = min(n, len(waters))
        random.shuffle(waters)

        to_freeze = waters[:n]
        for water in to_freeze:
            freeze(scene, water)

    def thaw_n(self, scene, n):
        logging.debug(f"EID#{self.entity}::FreezeWater thawing {n}")
        ices = scene.cm.get(IceTag, project=lambda it: it.entity)
        if not ices:
            return

        n = min(n, len(ices))
        random.shuffle(ices)

        to_thaw = ices[:n]
        for ice in to_thaw:
            thaw(scene, ice)

