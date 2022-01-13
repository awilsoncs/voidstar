from dataclasses import dataclass
from typing import Tuple

from engine.components.events import Event
from components.step_listeners.on_step_listener import StepListener


@dataclass
class StepEvent(Event):
    new_location: Tuple[int, int] = (-1, -1)

    def listener_type(self):
        return StepListener

    def notify(self, scene, listener):
        if listener.entity == self.entity:
            listener.on_step(scene, self.new_location)
