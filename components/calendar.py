from dataclasses import dataclass

from engine.component import Component

MAX_HOUR = 23
MAX_DAY = 30
MAX_SEASON = 4


@dataclass
class Calendar(Component):
    hour: int = 0
    day: int = 1
    season: int = 1
    year: int = 1217

    def increment(self):
        self.hour += 1
        if self.hour > MAX_HOUR:
            self.day += 1
            self.hour = 0

        if self.day > MAX_DAY:
            self.season += 1
            self.day = 0

        if self.season > MAX_SEASON:
            self.year += 1
            self.season = 0

    def get_timecode(self):
        return f'{self.hour}h {self.day}d {self.season}s {self.year}y'
