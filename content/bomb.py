from typing import List

from components import Coordinates, Appearance
from components.actors.bomb_actor import BombActor
from engine import core, palettes
from engine.components.component import Component
from engine.components.entity import Entity
from engine.constants import PRIORITY_LOW

bomb_description = "An explosive bomb! Watch out!"


def make_bomb(x, y):
    entity_id = core.get_id()
    components: List[Component] = [
        Entity(
            id=entity_id,
            entity=entity_id,
            name='bomb',
            description=bomb_description
        ),
        Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOW),
        Appearance(entity=entity_id, symbol='δ', color=palettes.MEAT, bg_color=palettes.BACKGROUND),
        BombActor(entity=entity_id)
    ]
    return entity_id, components

