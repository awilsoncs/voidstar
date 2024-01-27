from abc import abstractmethod, ABC
from dataclasses import dataclass

from components.abilities.ability import Ability
from components.animation_effects.blinker import AnimationBlinker
from engine.core import log_debug


@dataclass
class ControlModeAbility(Ability, ABC):
    @log_debug(__name__)
    def use(self, scene, dispatcher):
        sym, color = self.get_anim()
        mode = self.get_mode()
        new_controller = mode(entity=self.entity, old_brain=dispatcher)
        blinker = AnimationBlinker(
            entity=self.entity,
            new_symbol=sym,
            new_color=color
        )
        scene.cm.stash_component(dispatcher)
        scene.cm.add(new_controller, blinker)

    @abstractmethod
    def get_mode(self):
        pass

    @abstractmethod
    def get_anim(self):
        pass
