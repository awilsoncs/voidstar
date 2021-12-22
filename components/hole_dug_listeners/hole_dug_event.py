import logging
from dataclasses import dataclass
from typing import List

from components.actors.energy_actor import EnergyActor
from components.hole_dug_listeners.hole_dug_listener import HoleDugListener
from engine.core import log_debug


@dataclass
class HoleDugEvent(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT

    @log_debug(__name__)
    def act(self, scene):
        logging.info(f"EID#{self.entity}::HoleDugEvent hole dug")
        hole_dug_listeners: List[HoleDugListener] = scene.cm.get(HoleDugListener)
        for hole_dug_listener in hole_dug_listeners:
            hole_dug_listener.on_hole_dug(scene, self.entity)

        scene.cm.delete_component(self)
