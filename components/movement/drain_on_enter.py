from dataclasses import dataclass

from components.actions.attack_action import AttackAction
from components.events.step_event import EnterListener


@dataclass
class DrainOnEnter(EnterListener):
    """Whenever the owning entity takes a step into a water containing square, pick it up."""
    damage: int = 0

    def on_enter(self, scene, stepper):
        self._log_debug(f"entity stepped on")
        scene.cm.add(AttackAction(entity=self.entity, target=stepper, damage=self.damage))
