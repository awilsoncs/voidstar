from abc import ABC, abstractmethod

from engine.component import Component


class Actor(Component, ABC):
    def can_act(self) -> bool:
        """Return whether the actor is currently able to act."""
        return False

    @abstractmethod
    def act(self, scene) -> None:
        """Perform the actor's action."""
        raise NotImplementedError()

    @abstractmethod
    def pass_turn(self, delay=None) -> None:
        """Pass the turn, with a delay as necessary."""
        raise NotImplementedError()
