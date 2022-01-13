from abc import ABC, abstractmethod

from engine.components.component import Component


class StepListener(Component, ABC):
    """Trigger when the owning entity takes a step."""

    @abstractmethod
    def on_step(self, scene, point):
        raise NotImplementedError()
