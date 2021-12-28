from dataclasses import dataclass

from components import Coordinates
from components.abilities.ability import Ability
from components.animation_effects.blinker import AnimationBlinker
from components.brains.ranged_attack_actor import RangedAttackActor
from components.enums import Intention
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from components.tags.hordeling_tag import HordelingTag
from content.states import cant_shoot_animation, confused_animation
from engine.utilities import is_visible


@dataclass
class ShootAbility(SeasonResetListener, Ability):
    count: int = 5
    max: int = 5
    unlock_cost: int = 100
    use_cost: int = 0
    intention: Intention = Intention.SHOOT

    def on_season_reset(self, scene):
        self.count = self.max

    def use(self, scene, dispatcher):
        hordelings = [e for e in scene.cm.get(HordelingTag) if is_visible(scene, e.entity)]
        shoot_ability = scene.cm.get_one(ShootAbility, entity=self.entity)
        if shoot_ability and shoot_ability.count <= 0:
            self._handle_out_of_ammo(scene)
            return
        elif not hordelings:
            self._handle_confused(scene)
            return
        self._handle_shoot(scene, hordelings, dispatcher)

    def _handle_out_of_ammo(self, scene):
        player_coords = scene.cm.get_one(Coordinates, entity=self.entity)
        cant_shoot_anim = cant_shoot_animation(player_coords.x, player_coords.y)
        scene.cm.add(*cant_shoot_anim[1])

    def _handle_shoot(self, scene, hordelings, dispatcher):
        target = hordelings[0]
        new_controller = RangedAttackActor(
            entity=self.entity,
            old_actor=dispatcher,
            target=target.entity,
            shoot_ability=self.id
        )
        blinker = AnimationBlinker(entity=target.entity)
        scene.cm.stash_component(dispatcher)
        scene.cm.add(new_controller, blinker)

    def _handle_confused(self, scene):
        player_coords = scene.cm.get_one(Coordinates, entity=self.entity)
        confused_anim = confused_animation(player_coords.x, player_coords.y)
        scene.cm.add(*confused_anim[1])
