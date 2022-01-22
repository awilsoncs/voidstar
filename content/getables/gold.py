from components import Appearance, Coordinates
from components.material import Material
from components.pickup_gold import GoldPickup
from engine import core, palettes
from components.base_components.entity import Entity
from engine.constants import PRIORITY_LOW

description = "A gold nugget glimmers in the sun. Selling it will yield a fair bounty."


def make_gold_nugget(x, y):
    entity_id = core.get_id()

    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='gold nugget', description=description),
            Appearance(entity=entity_id, symbol='♦', color=palettes.GOLD, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOW),
            GoldPickup(entity=entity_id),
            Material(entity=entity_id, blocks=False, blocks_sight=False)
        ]
    )
