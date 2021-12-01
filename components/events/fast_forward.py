from calendar import Calendar
from dataclasses import dataclass

from components import TimedActor
from components.actors.calendar_actor import Calendar
from components.actors.energy_actor import EnergyActor
from engine import core
from engine.core import log_debug


@dataclass
class FastForward(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT

    @log_debug(__name__)
    def act(self, scene):
        calendar = scene.cm.get_one(Calendar, entity=core.get_id('calendar'))
        if calendar:
            calendar.day = 30
        scene.cm.delete_component(self)
