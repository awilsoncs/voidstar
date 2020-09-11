from calendar import Calendar
from dataclasses import dataclass

from components import TimedActor
from components.actors.calendar_actor import CalendarTimedActor
from engine import core
from engine.core import log_debug


@dataclass
class FastForward(TimedActor):
    timer_delay: int = TimedActor.REAL_TIME

    @log_debug(__name__)
    def act(self, scene):
        calendar = scene.cm.get_one(CalendarTimedActor, entity=core.get_id('calendar'))
        if calendar:
            calendar.day = 30
        scene.cm.delete_component(self)
