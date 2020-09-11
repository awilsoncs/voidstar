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
        return f'{get_day_section(self.hour)}, {self.day}d {self.season}s {self.year}y'


def get_day_section(hour):
    if hour < 4:
        return 'night'
    if hour < 8:
        return 'dawn'
    if hour < 11:
        return 'morning'
    if hour < 14:
        return 'noon'
    if hour < 17:
        return 'afternoon'
    if hour < 20:
        return 'evening'
    if hour <= 23:
        return 'night'

