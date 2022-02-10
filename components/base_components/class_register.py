from abc import ABC, abstractmethod
from dataclasses import dataclass

from components.base_components.component import Component
from components.base_components.events import Event
from engine import GameScene


@dataclass
class LoadClasses(Event):
    def listener_type(self):
        return LoadClassListener

    def notify(self, scene, listener: 'LoadClassListener'):
        listener.on_load_class(scene)

    def _after_notify(self, scene: GameScene) -> None:
        self._log_info(f"{len(Component.subclasses)} classes loaded")
        for clz in Component.subclasses:
            self._log_debug(f"loaded {clz}")


@dataclass
class LoadClassListener(Component, ABC):
    """A world building step."""

    @abstractmethod
    def on_load_class(self, scene):
        raise NotImplementedError()
