from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Tuple

from components import Coordinates
from components.base_components.component import Component
from components.base_components.events import Event
from engine import GameScene, constants


@dataclass
class StepEvent(Event):
    """Emitted when the owning entity takes a step."""
    new_location: Tuple[int, int] = (-1, -1)

    def listener_type(self):
        return StepListener

    def notify(self, scene, listener):
        if listener.entity == self.entity:
            listener.on_step(scene, self.new_location)

    def _after_notify(self, scene: GameScene) -> None:
        # emit entered events
        this_coords = scene.cm.get_one(Coordinates, entity=self.entity)
        enter_listeners = scene.cm.get(EnterListener)
        for enter_listener in enter_listeners:
            other_coords = scene.cm.get_one(Coordinates, entity=enter_listener.entity)
            if this_coords.is_at(other_coords):
                scene.cm.add(EnterEvent(entity=self.entity, entered=enter_listener.entity))


class StepListener(Component, ABC):
    """Trigger when the owning entity takes a step."""

    @abstractmethod
    def on_step(self, scene, point):
        raise NotImplementedError()


@dataclass
class EnterEvent(Event):
    """Emitted when the owning entity steps on another entity (if that entity cares)."""
    entered: int = constants.INVALID

    def listener_type(self):
        return EnterListener

    def notify(self, scene, listener):
        if listener.entity == self.entered:
            listener.on_enter(scene, self.entity)


class EnterListener(Component, ABC):
    """Trigger when an entity steps on the owning entity."""

    @abstractmethod
    def on_enter(self, scene, stepper):
        raise NotImplementedError()
