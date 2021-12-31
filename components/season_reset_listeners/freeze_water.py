import random
from dataclasses import dataclass

from components import Coordinates
from components.actors.calendar_actor import Calendar
from components.actors.energy_actor import EnergyActor
from components.attack_start_listeners.attack_start_actor import AttackStartListener
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from components.tags.ice_tag import IceTag
from components.tags.water_tag import WaterTag
from content.terrain.ice import make_ice
from content.terrain.water import make_water
from engine import core


@dataclass
class FreezeWater(EnergyActor, SeasonResetListener, AttackStartListener):
    energy_cost: int = EnergyActor.HALF_HOUR
    temperature: int = 10

    def on_season_reset(self, scene, season):
        if season == 'Winter':
            self.temperature = -5
        elif season == 'Spring':
            self.temperature = random.randint(1, 3)
        elif season == 'Summer':
            self.temperature = 10
        elif season == 'Fall':
            self.temperature = random.randint(1, 3)
        else:
            raise ValueError(f"EID#{self.entity}::FreezeWater.on_season_reset received bad season: {season}")

    def act(self, scene) -> None:
        if self.temperature < 0:
            for _ in range(self.temperature * -1):
                self.freeze_one(scene)
        else:
            for _ in range(self.temperature):
                self.thaw_one(scene)
        self.pass_turn()

    def freeze_one(self, scene):
        waters = scene.cm.get(WaterTag, project=lambda wt: wt.entity)
        if not waters:
            return
        to_freeze = random.choice(waters)
        self.freeze(scene, to_freeze)

    def freeze(self, scene, to_freeze):
        coords = scene.cm.get_one(Coordinates, entity=to_freeze)
        scene.cm.add(*make_ice(coords.x, coords.y)[1])
        scene.cm.delete(to_freeze)

    def thaw_one(self, scene):
        ices = scene.cm.get(IceTag, project=lambda it: it.entity)
        if not ices:
            return
        to_thaw = random.choice(ices)
        self.thaw(scene, to_thaw)

    def thaw(self, scene, to_thaw):
        coords = scene.cm.get_one(Coordinates, entity=to_thaw)
        scene.cm.add(*make_water(coords.x, coords.y)[1])
        scene.cm.delete(to_thaw)

    def freeze_all(self, scene):
        waters = scene.cm.get(WaterTag, project=lambda wt: wt.entity)
        for water in waters:
            self.freeze(scene, water)

    def thaw_all(self, scene):
        ices = scene.cm.get(IceTag, project=lambda it: it.entity)
        for ice in ices:
            self.thaw(scene, ice)

    def on_attack_start(self, scene):
        calendar = scene.cm.get_one(Calendar, entity=core.get_id("calendar"))
        season = calendar.get_season_string()
        if season in {"Spring", "Summer", "Fall"}:
            self.thaw_all(scene)
        else:
            self.freeze_all(scene)
