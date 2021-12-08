from dataclasses import dataclass

import tcod

from components.actors.energy_actor import EnergyActor
from components.animation_effects.blinker import AnimationBlinker
from components.enums import Intention
from components.tags.hordeling_tag import HordelingTag
from engine import core


@dataclass
class RangedAttackActor(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT
    old_actor: int = None
    target: int = 0

    def act(self, scene):
        self._handle_input(scene)

    def _handle_input(self, scene):
        key_event = core.get_key_event()
        if key_event:
            key_event = key_event.sym
            intention = KEY_ACTION_MAP.get(key_event, None)
            if intention is Intention.SHOOT:
                self.shoot(scene)
            elif intention in {
                Intention.STEP_NORTH,
                Intention.STEP_EAST,
                Intention.STEP_WEST,
                Intention.STEP_SOUTH
            }:
                self._next_enemy(scene)
            elif intention is Intention.BACK:
                scene.cm.unstash_component(self.old_actor)
                blinker = scene.cm.get_one(AnimationBlinker, entity=self.target)
                blinker.stop(scene)
                scene.cm.delete_component(blinker)
                scene.cm.delete_component(self)

    def _next_enemy(self, scene):
        next_enemy = self._get_next_enemy(scene)
        old_blinker = scene.cm.get_one(AnimationBlinker, entity=self.target)
        old_blinker.stop(scene)
        scene.cm.delete_component(old_blinker)
        scene.cm.add(AnimationBlinker(entity=next_enemy))
        self.target = next_enemy

    def _get_next_enemy(self, scene):
        current_target = scene.cm.get_one(HordelingTag, entity=self.target)
        enemies = sorted(scene.cm.get(HordelingTag), key=lambda x: x.id)
        index = enemies.index(current_target)
        next_index = (index + 1) % len(enemies)
        return enemies[next_index].entity


KEY_ACTION_MAP = {
    tcod.event.K_f: Intention.SHOOT,
    tcod.event.K_UP: Intention.STEP_NORTH,
    tcod.event.K_DOWN: Intention.STEP_SOUTH,
    tcod.event.K_RIGHT: Intention.STEP_EAST,
    tcod.event.K_LEFT: Intention.STEP_WEST,
    tcod.event.K_ESCAPE: Intention.BACK
}
