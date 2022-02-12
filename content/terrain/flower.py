from components import Appearance, Coordinates
from components.material import Material
from components.movement.die_on_enter import DieOnEnter
from engine import palettes, core
from components.base_components.entity import Entity
from engine.constants import PRIORITY_LOWEST


def make_flower(x, y, color):
    entity_id = core.get_id()

    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='flower'),
            Appearance(entity=entity_id, symbol='"', color=color, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOWEST, buildable=True),
            DieOnEnter(entity=entity_id),
            Material(entity=entity_id, blocks=False, blocks_sight=False)
        ]
    )
