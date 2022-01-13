from abc import ABC, abstractmethod

from engine.components.component import Component


class DallyListener(Component, ABC):
    """Trigger when the owning entity takes a step."""

    @abstractmethod
    def on_dally(self, scene):
        raise NotImplementedError()
