from dataclasses import dataclass

from engine.component import Component


@dataclass
class MasonryAbility(Component):
    ability_title: str = "Masonic Secrets"
