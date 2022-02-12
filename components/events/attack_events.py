from abc import ABC, abstractmethod
from dataclasses import dataclass

from components.base_components.component import Component
from components.base_components.events import Event


@dataclass
class AttackFinished(Event):
    """Emitted after an entity's attack has been processed."""
    def listener_type(self):
        return OnAttackFinishedListener

    def notify(self, scene, listener):
        listener.on_attack_finished(scene, self.entity)


@dataclass
class OnAttackFinishedListener(Component, ABC):
    @abstractmethod
    def on_attack_finished(self, scene, caller):
        raise NotImplementedError()
