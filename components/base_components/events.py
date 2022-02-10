from abc import abstractmethod
from dataclasses import dataclass

from engine import GameScene
from components.base_components.energy_actor import EnergyActor
from engine.core import log_debug


@dataclass
class Event(EnergyActor):
    """Define an event that notifies listeners."""
    energy_cost: int = EnergyActor.INSTANT

    @log_debug(__name__)
    def act(self, scene: GameScene) -> None:
        self._log_info("event")
        self._before_notify(scene)
        listeners = scene.cm.get(self.listener_type())
        for listener in listeners:
            self.notify(scene, listener)
        self._after_notify(scene)
        scene.cm.delete_component(self)
        self._after_remove(scene)

    @abstractmethod
    def listener_type(self):
        """Return the type of listener to notify."""
        raise NotImplementedError("Must subclass Event")

    @abstractmethod
    def notify(self, scene: GameScene, listener) -> None:
        """Notify a listener of the event."""
        raise NotImplementedError("Must subclass Event")

    def _before_notify(self, scene: GameScene) -> None:
        """Define actions to take before listeners have been notified."""
        pass

    def _after_notify(self, scene: GameScene) -> None:
        """Define actions to take after listeners have been notified but before deleting the event."""
        pass

    def _after_remove(self, scene: GameScene) -> None:
        pass
