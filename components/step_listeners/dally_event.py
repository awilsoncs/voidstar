from dataclasses import dataclass
from typing import Tuple, List

from components.actors.energy_actor import EnergyActor
from components.step_listeners.dally_listener import DallyListener
from engine.core import log_debug


@dataclass
class DallyEvent(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT

    @log_debug(__name__)
    def act(self, scene):
        listeners: List[DallyListener] = scene.cm.get_all(DallyListener, entity=self.entity)
        for listener in listeners:
            listener.on_dally(scene)
        scene.cm.delete_component(self)
