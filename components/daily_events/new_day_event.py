import logging
from dataclasses import dataclass
from typing import List

from components.actors.energy_actor import EnergyActor
from components.daily_events.new_day_listener import NewDayListener
from engine.core import log_debug


@dataclass
class NewDayBegan(EnergyActor):
    """Add this to an entity to have it delete itself after some time."""
    energy_cost: int = EnergyActor.INSTANT
    day: int = 0

    @log_debug(__name__)
    def act(self, scene):
        logging.debug(f"EID#{self.entity}:NewDay event")
        daily_listeners: List[NewDayListener] = scene.cm.get(NewDayListener)
        for listener in daily_listeners:
            listener.on_new_day(scene, self.day)

        scene.cm.delete_component(self)
