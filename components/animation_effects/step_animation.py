from dataclasses import dataclass, field
from typing import List

from components import Appearance
from components.base_components.timed_actor import TimedActor
from components.events.delete_event import Delete


@dataclass
class StepAnimation(TimedActor):
    """Flip the colors back and forth."""
    timer_delay: int = 90
    step: int = 0
    steps: List = field(default_factory=list)

    def act(self, scene):
        if self.step >= len(self.steps):
            scene.cm.add(Delete(entity=self.entity))
            self.pass_turn()
            return
        appearance = scene.cm.get_one(Appearance, entity=self.entity)
        appearance.symbol = self.steps[self.step][1]
        appearance.color = self.steps[self.step][0]
        self.step += 1
        self.pass_turn()
