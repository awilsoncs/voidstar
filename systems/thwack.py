from math import sqrt

from components.actions.attack_action import AttackAction
from components.actions.thwack_action import ThwackAction
from systems.utilities import get_enemies_in_range, retract_turn


def run(scene):
    """A thwack action applies the entity's attack to each adjacent enemy."""

    thwacks = scene.cm.get(ThwackAction)
    for thwack in thwacks:
        thwacker = thwack.entity

        # convert the thwack action to an attack action each adjacent enemy
        thwackables = get_enemies_in_range(scene, thwack.entity, max=2*sqrt(2))
        attacks = [
            AttackAction(entity=thwack.entity, recipient=t, damage=1)
            for t in thwackables
        ]

        for attack in attacks:
            scene.cm.add(attack)
        retract_turn(scene, thwacker)

    scene.cm.delete_components(ThwackAction)
