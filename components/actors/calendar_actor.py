from dataclasses import dataclass

from components.actors.energy_actor import EnergyActor
from components.actors.hordeling_spawner import HordelingSpawner
from components.actors.hordeling_spawner_spawner import HordelingSpawnerSpawner
from components.events.reset_season import ResetSeason
from components.tags import Tag
from content.spawners.hordeling_spawner_spawner import hordeling_spawner_spawner

MAX_HOUR = 23
MAX_DAY = 30
MAX_SEASON = 4


@dataclass
class Calendar(EnergyActor):
    hour: int = 0
    day: int = 1
    season: int = 1
    year: int = 1217
    status: str = "Peacetime"
    energy_cost: int = EnergyActor.DAILY
    round = 1

    def increment(self):
        self.hour += 24
        if self.hour > MAX_HOUR:
            self.day += 1
            self.hour = 0

        if self.day > MAX_DAY:
            self.season += 1
            self.day = 0

        if self.season > MAX_SEASON:
            self.year += 1
            self.season = 0
        self.pass_turn()

    def get_timecode(self):
        season = {
            1: "Spring",
            2: "Summer",
            3: "Autumn",
            4: "Winter"
        }[self.season]

        return f'{season} {self.day}d {self.year}y'

    def act(self, scene):

        if self.day < 25:
            self.status = "Peacetime"
            self.increment()
        elif self.day < 30:
            self.status = "Horde approaching..."
            self.increment()
        else:
            if self.status != "Under attack!":
                scene.popup_message("The Horde has arrived. Prepare to defend the village!")
                scene.cm.add(*hordeling_spawner_spawner(waves=self.round)[1])
                self.is_recharging = False
            self.status = "Under attack!"
            if not (
                scene.cm.get(HordelingSpawnerSpawner)
                or scene.cm.get(HordelingSpawner)
                or [t for t in scene.cm.get(Tag) if t.value == 'hordeling']
            ):
                self.status = "Peacetime"
                scene.cm.add(ResetSeason())
                self.round += 1
                self.is_recharging = True
                self.increment()
