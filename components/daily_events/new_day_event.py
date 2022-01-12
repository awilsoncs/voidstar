from dataclasses import dataclass

from components.daily_events.new_day_listener import NewDayListener
from components.events.events import Event


@dataclass
class NewDayBegan(Event):
    """Add this to an entity to have it delete itself after some time."""
    day: int = 0

    def listener_type(self):
        return NewDayListener

    def notify(self, scene, listener):
        listener.on_new_day(scene, self.day)
