from abc import ABC, abstractmethod
from dataclasses import dataclass

from engine.component import Component


@dataclass
class NewDayListener(Component, ABC):
    """A world building step."""

    @abstractmethod
    def on_new_day(self, scene, day):
        raise NotImplementedError()
