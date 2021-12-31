from abc import ABC, abstractmethod
from dataclasses import dataclass

from components import Coordinates
from components.enums import Intention
from content.states import no_money_animation
from engine import constants
from engine.component import Component


@dataclass
class Ability(Component, ABC):
    """Represent a Player ability."""
    unlock_cost: int = constants.INVALID
    use_cost: int = constants.INVALID
    intention: Intention = ''

    @abstractmethod
    def use(self, scene, dispatcher):
        raise NotImplementedError("Must subclass Ability")

    def apply(self, scene, dispatcher):
        if scene.gold < self.use_cost:
            self._handle_no_money(scene)
            return
        self.use(scene, dispatcher)

    def _handle_no_money(self, scene):
        player_coords = scene.cm.get_one(Coordinates, entity=self.entity)
        confused_anim = no_money_animation(player_coords.x, player_coords.y)
        scene.cm.add(*confused_anim[1])
