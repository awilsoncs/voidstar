from dataclasses import dataclass

from components import TimedActor
from components.calendar import Calendar
from engine import core
from systems.utilities import retract_turn


@dataclass
class CalendarTimedActor(TimedActor):
    active: bool = True
    timer_delay: int = TimedActor.HOURLY

    def act(self, scene):
        if self.active:
            calendar = scene.cm.get_one(Calendar, entity=core.get_id('calendar'))
            calendar.increment()
        retract_turn(scene, self.entity)
