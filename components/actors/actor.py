from engine.component import Component


class Actor(Component):
    def can_act(self) -> bool:
        """Return whether the actor is currently able to act."""
        return False

    def act(self, scene) -> None:
        """Perform the actor's action."""
        pass

    def pass_turn(self, delay=None) -> None:
        pass
