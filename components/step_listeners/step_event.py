from dataclasses import dataclass
from typing import Tuple, List

from components.actors.energy_actor import EnergyActor
from components.step_listeners.on_step_listener import StepListener
from engine.core import log_debug


@dataclass
class StepEvent(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT
    new_location: Tuple[int, int] = (-1, -1)

    @log_debug(__name__)
    def act(self, scene):
        step_listeners: List[StepListener] = scene.cm.get_all(StepListener, entity=self.entity)
        for step_listener in step_listeners:
            step_listener.on_step(scene, self.new_location)
        scene.cm.delete_component(self)
