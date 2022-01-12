from abc import abstractmethod
from dataclasses import dataclass
from typing import Type

from components.actors.energy_actor import EnergyActor
from engine.core import log_debug


@dataclass
class Event(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT

    @log_debug(__name__)
    def act(self, scene):
        self._before_notify(scene)
        listeners = scene.cm.get(self.listener_type())
        for listener in listeners:
            self._log_debug(f"notifying listener {listener.id}")
            self.notify(scene, listener)
        self._after_notify(scene)
        scene.cm.delete_component(self)

    @abstractmethod
    def listener_type(self):
        raise NotImplementedError("Must subclass Event")

    @abstractmethod
    def notify(self, scene, listener):
        raise NotImplementedError("Must subclass Event")

    def _before_notify(self, scene):
        """Define actions to take before listeners have been notified."""
        pass

    def _after_notify(self, scene):
        """Define actions to take after listeners have been notified but before deleting the event."""
        pass
