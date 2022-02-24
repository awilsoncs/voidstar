from dataclasses import dataclass

from components import Coordinates
from components.base_components.energy_actor import EnergyActor
from components.brains.brain import Brain
from components.animation_effects.blinker import AnimationBlinker
from components.events.peasant_events import PeasantDied
from components.stomach import Stomach
from content.states import sleep_animation
from engine import core, constants
from engine.core import log_debug


@dataclass
class SleepingBrain(Brain):
    turns: int = 3
    energy_cost: int = EnergyActor.HOURLY

    @log_debug(__name__)
    def act(self, scene):
        self._log_debug(f"sleeping one turn")
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        scene.cm.add(*sleep_animation(coords.x, coords.y)[1])
        self.pass_turn()
        if self.turns <= 0:
            self.back_out(scene)
        else:
            self.turns -= 1

    def _on_back_out(self, scene):
        stomach = scene.cm.get_one(Stomach, entity=self.entity)
        if stomach:
            if stomach.contents != constants.INVALID:
                self._log_debug(f"digested the peasant")
                scene.warn("A peasant has been lost!")
                scene.cm.add(PeasantDied(entity=core.get_id("world")))
            stomach.clear(scene)
