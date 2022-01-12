import logging
from dataclasses import dataclass

from components.abilities.ability import Ability
from components.abilities.null_ability import NullAbility
from components.events.attack_started_events import AttackStartListener


@dataclass
class AbilityTracker(AttackStartListener):
    current_ability: int = 0

    def on_attack_start(self, scene):
        self._log_debug("resetting ability to 0")
        self.current_ability = 0

    def get_current_ability(self, scene):
        abilities = scene.cm.get_all(Ability, entity=self.entity)
        if not abilities:
            return NullAbility()
        index = self.current_ability % len(abilities)
        return abilities[index]

    def increment(self, scene):
        abilities = scene.cm.get_all(Ability, entity=self.entity)
        self.current_ability = (self.current_ability + 1) % len(abilities)
        ability = abilities[self.current_ability]
        self._log_debug(f"increment {self.current_ability} - {ability.ability_title}")

    def decrement(self, scene):
        abilities = scene.cm.get_all(Ability, entity=self.entity)
        self.current_ability = (self.current_ability - 1) % len(abilities)
        ability = abilities[self.current_ability]
        self._log_debug(f"decrement {self.current_ability} - {ability.ability_title}")

