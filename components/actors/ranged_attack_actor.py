from dataclasses import dataclass

import tcod

from components.actors.energy_actor import EnergyActor
from components.animation_effects.blinker import AnimationBlinker
from components.enums import Intention
from engine import core


@dataclass
class RangedAttackActor(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT
    old_actor: int = None
    target: int = None

    def act(self, scene):
        self._handle_input(scene)
        self._update_target(scene)

    def _handle_input(self, scene):
        key_event = core.get_key_event()
        if key_event:
            key_event = key_event.sym
            intention = KEY_ACTION_MAP.get(key_event, None)
            if intention is Intention.SHOOT:
                print("shoot")
            elif intention is Intention.BACK:
                old_actor = scene.cm.unstash_component(self.old_actor)
                scene.cm.add(old_actor)
                blinker = scene.cm.get_one(AnimationBlinker, entity=self.entity)
                blinker.stop(scene)
                scene.cm.delete_component(blinker)
                scene.cm.delete_component(self)

    def _update_target(self, scene):
        pass


KEY_ACTION_MAP = {
    tcod.event.K_f: Intention.SHOOT,
    tcod.event.K_ESCAPE: Intention.BACK
}
