from dataclasses import dataclass

from components.actors.energy_actor import EnergyActor
from components.actors.hordeling_spawner import HordelingSpawner
from components.actors.hordeling_spawner import HordelingSpawner
from components.attack_start_listeners.start_attack import StartAttack
from components.daily_events.new_day_event import NewDayBegan
from components.season_reset_listeners.reset_season import ResetSeason
from components.tags.hordeling_tag import HordelingTag
from content.spawners.hordeling_spawner_spawner import hordeling_spawner

MAX_HOUR = 23
MAX_DAY = 30
MAX_SEASON = 4


@dataclass
class Calendar(EnergyActor):
    day: int = 0
    season: int = 1
    year: int = 1217
    status: str = "Peacetime"
    energy_cost: int = EnergyActor.DAILY
    round = 1

    def increment(self):
        self.day += 1
        if self.day > MAX_DAY:
            self.season += 1
            self.day = 1

        if self.season > MAX_SEASON:
            self.year += 1
            self.season = 1
        self.pass_turn()

    def get_timecode(self):
        season = self.get_season_string()

        return f'{season} {self.day}d {self.year}y'

    def get_season_string(self):
        return {
            1: "Spring",
            2: "Summer",
            3: "Fall",
            4: "Winter"
        }[self.season]

    def act(self, scene):
        if self.day < 25:
            self.status = "Peacetime"
            self.increment()
            scene.cm.add(NewDayBegan(entity=self.entity, day=self.day))
        elif self.day < 30:
            self.status = "Horde approaching..."
            self.increment()
            scene.cm.add(NewDayBegan(entity=self.entity, day=self.day))
        else:
            if self.status != "Under attack!":
                self._start_attack(scene)
            if not still_under_attack(scene):
                self._end_attack(scene)

    def _start_attack(self, scene):
        scene.popup_message("The Horde has arrived. Prepare to defend the village!")
        scene.cm.add(*hordeling_spawner(waves=self.round)[1])
        scene.cm.add(StartAttack(entity=scene.player))
        self.is_recharging = False
        self.status = "Under attack!"

    def _end_attack(self, scene):
        self.status = "Peacetime"
        self.round += 1
        self.is_recharging = True
        self.increment()
        scene.cm.add(NewDayBegan(entity=self.entity))
        scene.cm.add(ResetSeason(entity=self.entity, season=self.get_season_string()))


def still_under_attack(scene):
    return (
        scene.cm.get(HordelingSpawner)
        or scene.cm.get(HordelingSpawner)
        or [t for t in scene.cm.get(HordelingTag)]
    )
