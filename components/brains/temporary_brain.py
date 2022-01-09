from abc import ABC
from dataclasses import dataclass

from components.animation_effects.blinker import AnimationBlinker
from components.brains.brain import Brain
from engine import constants


@dataclass
class TemporaryBrain(Brain, ABC):
    """Provides brain recovery functionality."""
    old_actor: int = constants.INVALID

    def back_out(self, scene):
        old_actor = scene.cm.unstash_component(self.old_actor)
        blinker = scene.cm.get_one(AnimationBlinker, entity=self.entity)
        if blinker:
            blinker.stop(scene)
            scene.cm.delete_component(blinker)
        scene.cm.delete_component(self)
        return old_actor
