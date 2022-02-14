from typing import List

from components import Coordinates, Appearance
from components.animation_effects.step_animation import StepAnimation
from components.base_components.component import Component
from components.base_components.entity import Entity
from engine import core, palettes
from engine.constants import PRIORITY_LOW


def make_explosion(x, y):
    entity_id = core.get_id()
    components: List[Component] = [
        Entity(
            id=entity_id,
            entity=entity_id,
            name='explosion',
            description="The air has ignited here."
        ),
        Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOW),
        Appearance(entity=entity_id, symbol='*', color=palettes.WHITE, bg_color=palettes.BACKGROUND),
        StepAnimation(
            entity=entity_id,
            steps=[
                (palettes.GOLD, '*'),
                (palettes.FRESH_BLOOD, '*')
            ]
        )
    ]
    return entity_id, components
