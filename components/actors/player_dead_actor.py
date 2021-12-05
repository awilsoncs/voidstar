from dataclasses import dataclass

import tcod

from components.abilities.thwack_ability import ThwackAbility
from components.actions.thwack_action import ThwackAction
from components.actors.energy_actor import EnergyActor
from components.enums import Intention
from components.events.chargeabilityevent import ChargeAbilityEvent
from components.events.fast_forward import FastForward
from engine import core
from systems.utilities import set_intention


@dataclass
class PlayerDeadActor(EnergyActor):

    def act(self, scene):
        handle_key_event(scene, self.entity, DEAD_KEY_ACTION_MAP)


def handle_key_event(scene, entity_id, action_map):
    key_event = core.get_key_event()
    if key_event:
        key_event = key_event.sym
        intention = action_map.get(key_event, None)
        if intention is not None:
            set_intention(scene, entity_id, None, intention)


DEAD_KEY_ACTION_MAP = {
    tcod.event.K_BACKQUOTE: Intention.SHOW_DEBUG_SCREEN,
    tcod.event.K_ESCAPE: Intention.QUIT_GAME
}