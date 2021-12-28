from dataclasses import dataclass

import tcod

from components import Coordinates
from components.abilities.ability import Ability
from components.enums import Intention
from components.brains.brain import Brain
from components.states.dizzy_state import DizzyState
from content.states import confused_animation
from engine import core


@dataclass
class PlayerBrain(Brain):
    def act(self, scene):
        dizzy = scene.cm.get_one(DizzyState, entity=self.entity)
        if dizzy:
            core.get_key_event()
            if core.time_ms() > dizzy.next_turn:
                self.intention = Intention.DALLY
                dizzy.next_turn = core.time_ms() + 500
                dizzy.duration -= 1
                coords = scene.cm.get_one(Coordinates, entity=self.entity)
                scene.cm.add(*confused_animation(coords.x, coords.y)[1])

                if dizzy.duration <= 0:
                    scene.cm.delete_component(dizzy)
        else:
            self.handle_key_event(scene, KEY_ACTION_MAP)

    def handle_key_event(self, scene, action_map):
        key_event = core.get_key_event()
        if key_event:
            key_event = key_event.sym
            intention = action_map.get(key_event, None)
            abilities = {a.intention: a for a in scene.cm.get_all(Ability, entity=self.entity)}
            if intention in abilities:
                # todo Migrate all of this to a component definition system
                if intention in abilities:
                    ability = abilities[intention]
                    if not ability:
                        self._handle_confused(scene)
                        return
                    ability.apply(scene, self.id)
            elif intention is None:
                return
            else:
                self.intention = intention

    def _handle_confused(self, scene):
        player_coords = scene.cm.get_one(Coordinates, entity=self.entity)
        confused_anim = confused_animation(player_coords.x, player_coords.y)
        scene.cm.add(*confused_anim[1])


KEY_ACTION_MAP = {
    tcod.event.K_a: Intention.FAST_FORWARD,
    tcod.event.K_f: Intention.SHOOT,
    tcod.event.K_s: Intention.PLANT_SAPLING,
    tcod.event.K_d: Intention.DIG_HOLE,
    tcod.event.K_l: Intention.LOOK,
    tcod.event.K_e: Intention.BUILD_FENCE,
    tcod.event.K_r: Intention.BUILD_WALL,
    tcod.event.K_c: Intention.SELL,
    tcod.event.K_UP: Intention.STEP_NORTH,
    tcod.event.K_DOWN: Intention.STEP_SOUTH,
    tcod.event.K_RIGHT: Intention.STEP_EAST,
    tcod.event.K_LEFT: Intention.STEP_WEST,
    tcod.event.K_PERIOD: Intention.DALLY,
    tcod.event.K_SPACE: Intention.THWACK,

    tcod.event.K_BACKQUOTE: Intention.SHOW_DEBUG_SCREEN,
    tcod.event.K_ESCAPE: Intention.BACK
}
