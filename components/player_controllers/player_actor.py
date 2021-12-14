from dataclasses import dataclass

import tcod

from components import Coordinates
from components.abilities.shoot_ability import ShootAbility
from components.abilities.thwack_ability import ThwackAbility
from components.actions.thwack_action import ThwackAction
from components.actors.energy_actor import EnergyActor
from components.player_controllers.plant_sapling_actor import PlantSaplingActor
from components.player_controllers.ranged_attack_actor import RangedAttackActor
from components.animation_effects.blinker import AnimationBlinker
from components.enums import Intention
from components.events.chargeabilityevent import ChargeAbilityEvent
from components.events.fast_forward import FastForward
from components.states.dizzy_state import DizzyState
from components.tags.hordeling_tag import HordelingTag
from content.states import confused_animation, cant_shoot_animation, no_money_animation
from engine import core, palettes
from engine.utilities import is_visible
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
                scene.cm.add(*confused_animation(coords.x, coords.y)[1])

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
                # todo Migrate all of this to a component definition system
                if intention is Intention.FAST_FORWARD:
                    # fast forwards are migrated to a new actor system
                    # todo Migrate FastForward to a player controller
                    scene.cm.add(FastForward())
                elif intention is Intention.SHOOT:
                    hordelings = [e for e in scene.cm.get(HordelingTag) if is_visible(scene, e.entity)]
                    shoot_ability = scene.cm.get_one(ShootAbility, entity=self.entity)
                    if shoot_ability and shoot_ability.count <= 0:
                        self._handle_out_of_ammo(scene)
                        return
                    elif not hordelings:
                        self._handle_no_enemies(scene)
                        return
                    self._handle_shoot(entity_id, hordelings, scene)
                elif intention is Intention.PLANT_SAPLING:
                    if scene.gold < 2:
                        self._handle_no_money(scene)
                        return
                    self._handle_plant_sapling(entity_id, scene)
                else:
                    set_intention(scene, entity_id, None, intention)
            else:
                # new event-based actions
                if int(key_event) is tcod.event.K_SPACE:
                    ability = scene.cm.get_one(ThwackAbility, entity=entity_id)
                    if ability:
                        scene.cm.add(ThwackAction(entity=entity_id))
            scene.cm.add(ChargeAbilityEvent(entity=entity_id))

    def _handle_out_of_ammo(self, scene):
        player_coords = scene.cm.get_one(Coordinates, entity=self.entity)
        cant_shoot_anim = cant_shoot_animation(player_coords.x, player_coords.y)
        scene.cm.add(*cant_shoot_anim[1])

    def _handle_no_enemies(self, scene):
        player_coords = scene.cm.get_one(Coordinates, entity=self.entity)
        confused_anim = confused_animation(player_coords.x, player_coords.y)
        scene.cm.add(*confused_anim[1])

    def _handle_shoot(self, entity_id, hordelings, scene):
        target = hordelings[0]
        new_controller = RangedAttackActor(entity=entity_id, old_actor=self.id, target=target.entity)
        blinker = AnimationBlinker(entity=target.entity)
        scene.cm.stash_component(self.id)
        scene.cm.add(new_controller, blinker)

    def _handle_no_money(self, scene):
        player_coords = scene.cm.get_one(Coordinates, entity=self.entity)
        confused_anim = no_money_animation(player_coords.x, player_coords.y)
        scene.cm.add(*confused_anim[1])

    def _handle_plant_sapling(self, entity_id, scene):
        new_controller = PlantSaplingActor(entity=entity_id, old_actor=self.id)
        blinker = AnimationBlinker(
            entity=self.entity,
            new_symbol='+',
            new_color=palettes.FOILAGE_C
        )
        scene.cm.stash_component(self.id)
        scene.cm.add(new_controller, blinker)


KEY_ACTION_MAP = {
    tcod.event.K_a: Intention.FAST_FORWARD,
    tcod.event.K_f: Intention.SHOOT,
    tcod.event.K_s: Intention.PLANT_SAPLING,
    tcod.event.K_UP: Intention.STEP_NORTH,
    tcod.event.K_DOWN: Intention.STEP_SOUTH,
    tcod.event.K_RIGHT: Intention.STEP_EAST,
    tcod.event.K_LEFT: Intention.STEP_WEST,
    tcod.event.K_PERIOD: Intention.DALLY,

    tcod.event.K_BACKQUOTE: Intention.SHOW_DEBUG_SCREEN,
    tcod.event.K_ESCAPE: Intention.BACK
}
