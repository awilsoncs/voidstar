from dataclasses import dataclass

from components import Coordinates
from components.attack_effect.attack_effect import AttackEffect


@dataclass
class KnockbackAttack(AttackEffect):
    def apply(self, scene, source, target):
        print("Juggernaut knocked back target!")
        source_coords = scene.cm.get_one(Coordinates, entity=source)
        target_coords = scene.cm.get_one(Coordinates, entity=target)

        direction = source_coords.direction_towards(target_coords)
        target_coords.x += direction[0]
        target_coords.y += direction[1]
