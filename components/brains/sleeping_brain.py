import logging
from dataclasses import dataclass

from components import Coordinates
from components.actors.energy_actor import EnergyActor
from components.brains.temporary_brain import TemporaryBrain
from content.states import sleep_animation
from engine.core import log_debug


@dataclass
class SleepingBrain(TemporaryBrain):
    turns: int = 3
    energy_cost: int = EnergyActor.HOURLY

    @log_debug(__name__)
    def act(self, scene):
        logging.debug(f"EID#{self.entity}::SleepingBrain sleeping one turn")
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        scene.cm.add(*sleep_animation(coords.x, coords.y)[1])
        self.pass_turn()
        if self.turns <= 0:
            self.back_out(scene)
        else:
            self.turns -= 1
