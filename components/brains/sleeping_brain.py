import logging
from dataclasses import dataclass

from components import Coordinates
from components.actors.energy_actor import EnergyActor
from components.animation_effects.blinker import AnimationBlinker
from components.brains.temporary_brain import TemporaryBrain
from components.stomach import Stomach
from content.states import sleep_animation
from engine.core import log_debug


@dataclass
class SleepingBrain(TemporaryBrain):
    turns: int = 3
    energy_cost: int = EnergyActor.HOURLY

    @log_debug(__name__)
    def act(self, scene):
        self._log_debug(f"sleeping one turn")
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        scene.cm.add(*sleep_animation(coords.x, coords.y)[1])
        self.pass_turn()
        if self.turns <= 0:
            blinker = scene.cm.get_one(AnimationBlinker, entity=self.entity)
            if blinker:
                blinker.stop(scene)
                scene.cm.delete_component(blinker)
            stomach = scene.cm.get_one(Stomach, entity=self.entity)
            if stomach:
                stomach.clear(scene)

            self.back_out(scene)

        else:
            self.turns -= 1
