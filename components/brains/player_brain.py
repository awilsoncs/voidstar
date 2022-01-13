from dataclasses import dataclass

import tcod

from components.ability_tracker import AbilityTracker
from components.enums import Intention
from components.brains.brain import Brain
from components.events.quit_game_events import QuitGame
from components.events.show_help_dialogue import ShowHelpDialogue
from engine import core


@dataclass
class PlayerBrain(Brain):
    def act(self, scene):
        action_map = KEY_ACTION_MAP
        key_event = core.get_key_event()
        if key_event:
            self._log_debug(f"received input {key_event}")
            key_code = key_event.sym
            intention = action_map.get(key_code, None)
            self._log_debug(f"translated {key_event} -> {intention}")

            tracker = scene.cm.get_one(AbilityTracker, entity=self.entity)
            if intention == Intention.NEXT_ABILITY:
                tracker.increment(scene)
            elif intention == Intention.PREVIOUS_ABILITY:
                tracker.decrement(scene)
            elif intention == Intention.USE_ABILITY:
                ability = tracker.get_current_ability(scene)
                ability.apply(scene, self.id)
            elif intention == Intention.SHOW_HELP:
                scene.cm.add(ShowHelpDialogue(entity=self.entity))
            elif intention == Intention.BACK:
                scene.cm.add(QuitGame(entity=self.entity))
            elif intention is None:
                self._log_debug(f"found no useable intention")
                return
            else:
                self._log_debug(f"deferred intention {intention} (usually for movement intentions)")
                self.intention = intention


KEY_ACTION_MAP = {
    tcod.event.K_e: Intention.NEXT_ABILITY,
    tcod.event.K_q: Intention.PREVIOUS_ABILITY,
    tcod.event.K_SPACE: Intention.USE_ABILITY,
    tcod.event.K_h: Intention.SHOW_HELP,

    tcod.event.K_UP: Intention.STEP_NORTH,
    tcod.event.K_DOWN: Intention.STEP_SOUTH,
    tcod.event.K_RIGHT: Intention.STEP_EAST,
    tcod.event.K_LEFT: Intention.STEP_WEST,
    tcod.event.K_PERIOD: Intention.DALLY,

    tcod.event.K_ESCAPE: Intention.BACK
}
