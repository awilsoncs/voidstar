from dataclasses import dataclass

import tcod

from components import Coordinates
from components.abilities.shoot_ability import ShootAbility
from components.abilities.thwack_ability import ThwackAbility
from components.actions.thwack_action import ThwackAction
from components.actors.energy_actor import EnergyActor
from components.actors.ranged_attack_actor import RangedAttackActor
from components.animation_effects.blinker import AnimationBlinker
from components.enums import Intention
from components.events.chargeabilityevent import ChargeAbilityEvent
from components.events.fast_forward import FastForward
from components.states.dizzy_state import DizzyState
from components.tags.hordeling_tag import HordelingTag
from content.states import dizzy_animation
from engine import core
from systems.utilities import set_intention


@dataclass
class PlayerActor(EnergyActor):

    def act(self, scene):
        dizzy = scene.cm.get_one(DizzyState, entity=self.entity)
        if dizzy:
            core.get_key_event()
            if core.time_ms() > dizzy.next_turn:
                set_intention(scene, self.entity, None, Intention.DALLY)
                scene.cm.add(ChargeAbilityEvent(entity=self.entity))
                dizzy.next_turn = core.time_ms() + 500
                dizzy.duration -= 1

                coords = scene.cm.get_one(Coordinates, entity=self.entity)
                scene.cm.add(*dizzy_animation(self.entity, coords.x, coords.y)[1])

                if dizzy.duration <= 0:
                    scene.cm.delete_component(dizzy)
        else:
            self.handle_key_event(scene, self.entity, KEY_ACTION_MAP)

    def handle_key_event(self, scene, entity_id, action_map):
        key_event = core.get_key_event()
        if key_event:
            key_event = key_event.sym
            intention = action_map.get(key_event, None)
            if intention is not None:
                if intention is Intention.FAST_FORWARD:
                    # fast forwards are migrated to a new actor system
                    scene.cm.add(FastForward())
                elif intention is Intention.SHOOT:
                    hordelings = scene.cm.get(HordelingTag)
                    shoot_ability = scene.cm.get_one(ShootAbility, entity=self.entity)
                    if not hordelings or not shoot_ability or not shoot_ability.count > 0:
                        return
                    self._handle_shoot(entity_id, hordelings, scene)
                else:
                    set_intention(scene, entity_id, None, intention)
            else:
                # new event-based actions
                if int(key_event) is tcod.event.K_SPACE:
                    ability = scene.cm.get_one(ThwackAbility, entity=entity_id)
                    if ability:
                        scene.cm.add(ThwackAction(entity=entity_id))
            scene.cm.add(ChargeAbilityEvent(entity=entity_id))

    def _handle_shoot(self, entity_id, hordelings, scene):
        target = hordelings[0].entity
        new_controller = RangedAttackActor(entity=entity_id, old_actor=self.id, target=target)
        blinker = AnimationBlinker(entity=target)
        scene.cm.stash_component(self.id)
        scene.cm.add(new_controller, blinker)


KEY_ACTION_MAP = {
    tcod.event.K_a: Intention.FAST_FORWARD,
    tcod.event.K_f: Intention.SHOOT,
    tcod.event.K_UP: Intention.STEP_NORTH,
    tcod.event.K_DOWN: Intention.STEP_SOUTH,
    tcod.event.K_RIGHT: Intention.STEP_EAST,
    tcod.event.K_LEFT: Intention.STEP_WEST,
    tcod.event.K_PERIOD: Intention.DALLY,

    tcod.event.K_BACKQUOTE: Intention.SHOW_DEBUG_SCREEN,
    tcod.event.K_ESCAPE: Intention.BACK
}
