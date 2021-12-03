from abc import ABC, abstractmethod

from engine.component import Component


class AttackStartListener(Component, ABC):
    """Define a step to take when an attack starts."""
    @abstractmethod
    def on_attack_start(self, scene):
        raise NotImplementedError()
