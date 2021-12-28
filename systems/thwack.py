from math import sqrt

from components.abilities.thwack_ability import ThwackAbility
from components.events.chargeabilityevent import ChargeAbilityEvent
from components.actions.thwack_action import ThwackAction


def handle_thwack_ability(scene, thwack_ability):
    thwack_actions = scene.cm.get_all(ThwackAction, entity=thwack_ability.entity)

    if not thwack_actions and scene.cm.get_one(ChargeAbilityEvent, entity=thwack_ability.entity):
        thwack_ability.count = min(thwack_ability.count + 1, thwack_ability.max)

    for thwack in thwack_actions:
        handle_thwack_action(scene, thwack)


def run(scene):
    """A thwack action applies the entity's attack to each adjacent enemy."""
    thwack_abilities = scene.cm.get(ThwackAbility)
    for thwack_ability in thwack_abilities:
        handle_thwack_ability(scene, thwack_ability)
    scene.cm.delete_components(ThwackAction)
