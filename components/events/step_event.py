from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Tuple

from components.base_components.component import Component
from components.base_components.events import Event


@dataclass
class StepEvent(Event):
    new_location: Tuple[int, int] = (-1, -1)

    def listener_type(self):
        return StepListener

    def notify(self, scene, listener):
        if listener.entity == self.entity:
            listener.on_step(scene, self.new_location)


class StepListener(Component, ABC):
    """Trigger when the owning entity takes a step."""

    @abstractmethod
    def on_step(self, scene, point):
        raise NotImplementedError()
