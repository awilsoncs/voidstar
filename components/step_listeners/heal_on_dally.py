from dataclasses import dataclass

from components import Attributes
from components.attack_start_listeners.attack_start_actor import AttackStartListener
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from components.step_listeners.dally_listener import DallyListener
from engine import palettes


@dataclass
class HealOnDally(DallyListener, AttackStartListener, SeasonResetListener):
    count: int = 0
    heal_count: int = 5

    def on_dally(self, scene):
        self.count = (self.count + 1) % self.heal_count
        if self.count == 0:
            attributes = scene.cm.get_one(Attributes, entity=self.entity)
            if attributes.hp < attributes.max_hp:
                attributes.hp = min(attributes.hp+1, attributes.max_hp)
                scene.message("You rest and your wounds heal.", color=palettes.WHITE)

    def on_season_reset(self, scene, season):
        self.count = 0

    def on_attack_start(self, scene):
        self.count = 0
