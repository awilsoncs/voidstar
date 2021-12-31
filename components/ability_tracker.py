import logging
from dataclasses import dataclass

from components.abilities.ability import Ability
from engine.component import Component


@dataclass
class AbilityTracker(Component):
    current_ability: int = 0

    def get_current_ability(self, scene):
        abilities = scene.cm.get_all(Ability, entity=scene.player)
        index = self.current_ability % len(abilities)
        return abilities[index]

    def increment(self, scene):
        abilities = scene.cm.get_all(Ability, entity=scene.player)
        self.current_ability = (self.current_ability + 1) % len(abilities)
        ability = abilities[self.current_ability]
        logging.debug(f"EID#{self.entity}::AbilityTracker increment {self.current_ability} - {ability.ability_title}")

    def decrement(self, scene):
        abilities = scene.cm.get_all(Ability, entity=scene.player)
        self.current_ability = (self.current_ability - 1) % len(abilities)
        ability = abilities[self.current_ability]
        logging.debug(f"EID#{self.entity}::AbilityTracker decrement {self.current_ability} - {ability.ability_title}")

