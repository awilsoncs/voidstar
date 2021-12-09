import random
from dataclasses import dataclass

from components import Coordinates
from components.actions.attack_action import AttackAction
from components.actors.energy_actor import EnergyActor
from components.attack import Attack
from components.target_value import TargetValue
from engine.core import log_debug
from components.actors import VECTOR_STEP_MAP, STEPS
from systems.utilities import set_intention


@dataclass
class MonsterActor(EnergyActor):

    @log_debug(__name__)
    def act(self, scene):
        # find all possible targets
        targets = [t.entity for t in scene.cm.get(TargetValue)]
        if targets:
            # find the closest one
            owner_coord = scene.cm.get_one(Coordinates, entity=self.entity)
            related_coords = [
                scene.cm.get_one(Coordinates, entity=e)
                for e in targets
            ]
            sorted_coords = sorted(related_coords, key=lambda c: c.distance_from(owner_coord))
            closest_target = sorted_coords[0]

            # < 2 allows diagonal attacks
            if owner_coord.distance_from(closest_target) < 2:
                attack = scene.cm.get_one(Attack, entity=self.entity)
                scene.cm.add(
                    AttackAction(
                        entity=self.entity,
                        recipient=closest_target.entity,
                        damage=attack.damage
                    )
                )
            else:
                # get the direction to step towards it
                direction = owner_coord.direction_towards(closest_target)
                # set the intention
                step_intention = VECTOR_STEP_MAP[direction]
                set_intention(scene, self.entity, 0, step_intention)
        else:
            set_intention(scene, self.entity, 0, random.choice(STEPS))
