from dataclasses import dataclass

from components.events.die_events import Die
from components.events.step_event import EnterListener


@dataclass
class DieOnEnter(EnterListener):
    """Whenever the owning entity is stepped on, it dies."""

    def on_enter(self, scene, stepper):
        self._log_debug(f"entity stepped on")
        scene.cm.add(Die(entity=self.entity, killer=stepper))
