from dataclasses import dataclass

from components import Attributes
from components.events.attack_started_events import AttackStartListener
from components.events.dally_event import DallyListener
from engine import palettes


@dataclass
class HealOnDally(DallyListener, AttackStartListener):
    count: int = 0
    heal_count: int = 5

    def on_dally(self, scene):
        self.count = (self.count + 1) % self.heal_count
        if self.count == 0:
            attributes = scene.cm.get_one(Attributes, entity=self.entity)
            if attributes.hp < attributes.max_hp:
                attributes.hp = min(attributes.hp+1, attributes.max_hp)
                scene.message("You rest and your wounds heal.", color=palettes.WHITE)

    def on_attack_start(self, scene):
        self.count = 0
