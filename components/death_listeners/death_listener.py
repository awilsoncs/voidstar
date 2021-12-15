from abc import ABC, abstractmethod

from engine.component import Component


class DeathListener(Component, ABC):
    """Called when the entity dies."""
    @abstractmethod
    def on_die(self, scene):
        raise NotImplementedError()
