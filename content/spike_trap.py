from components import Appearance, Coordinates
from engine.components.entity import Entity
from components.die_on_attack_finished import DieOnAttackFinished
from components.diggable import Diggable
from components.material import Material
from components.movement.drain_on_enter import DrainOnEnter
from components.states.move_cost_affectors import DifficultTerrain
from engine import core, palettes
from engine.constants import PRIORITY_LOWEST


def make_spike_trap(x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='spike trap'),
            Appearance(entity=entity_id, symbol='╨', color=palettes.STONE, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOWEST),
            Material(entity=entity_id, blocks=False, blocks_sight=False),
            DifficultTerrain(entity=entity_id),
            Diggable(entity=entity_id),
            DrainOnEnter(entity=entity_id, damage=3),
            DieOnAttackFinished(entity=entity_id)
        ]
    )
