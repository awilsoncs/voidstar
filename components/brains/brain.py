from abc import ABC
from dataclasses import dataclass

from components.animation_effects.blinker import AnimationBlinker
from components.base_components.energy_actor import EnergyActor
from engine import GameScene, constants


@dataclass
class Brain(EnergyActor, ABC):
    # Establish a brain stack
    old_brain: int = constants.INVALID

    def swap(self, scene: GameScene, new_brain: 'Brain') -> None:
        """Swap this brain with a new brain."""
        new_brain.old_brain = self.id
        scene.cm.stash_component(self.id)
        scene.cm.add(new_brain)

    def back_out(self, scene):
        old_actor = scene.cm.unstash_component(self.old_brain)
        # todo not sure if this is a great place for this
        blinker = scene.cm.get_one(AnimationBlinker, entity=self.entity)
        if blinker:
            blinker.stop(scene)
            scene.cm.delete_component(blinker)
        scene.cm.delete_component(self)
        return old_actor

