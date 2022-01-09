from dataclasses import dataclass

from components import Coordinates
from components.abilities.ability import Ability
from components.animation_effects.blinker import AnimationBlinker
from components.brains.ranged_attack_actor import RangedAttackActor
from components.enums import Intention
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from components.tags.hordeling_tag import HordelingTag
from content.states import confused_animation
from engine.utilities import is_visible


@dataclass
class ShootAbility(SeasonResetListener, Ability):
    ability_title: str = "Shoot Bow"
    count: int = 5
    max: int = 5
    unlock_cost: int = 100
    use_cost: int = 5

    def on_season_reset(self, scene, season):
        self.count = self.max

    def use(self, scene, dispatcher):
        hordelings = [e for e in scene.cm.get(HordelingTag) if is_visible(scene, e.entity)]
        if not hordelings:
            self._handle_confused(scene)
            return
        self._handle_shoot(scene, hordelings, dispatcher)

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
        # todo why are we removing gold in the ability? You may have declined to shoot.
        scene.gold -= 5

    def _handle_confused(self, scene):
        player_coords = scene.cm.get_one(Coordinates, entity=self.entity)
        confused_anim = confused_animation(player_coords.x, player_coords.y)
        scene.cm.add(*confused_anim[1])
