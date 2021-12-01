from components import Entity, Appearance, Attributes, Coordinates
from components.corpse import Corpse
from components.faction import Faction
from components.material import Material
from engine import core, palettes
from engine.constants import PRIORITY_MEDIUM


def make_wall(zone_id, x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='wall', zone=zone_id),
            Appearance(entity=entity_id, symbol='#', color=palettes.STRAW, bg_color=palettes.BACKGROUND),
            Corpse(entity=entity_id, symbol='%', color=palettes.STRAW, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_MEDIUM),
            Attributes(entity=entity_id, hp=10, max_hp=10),
            Faction(entity=entity_id, faction=Faction.Options.PEASANT),
            Material(entity=entity_id, blocks=True, blocks_sight=False)
        ]
    )


def make_house(zone_id, x, y):
    return [
        make_wall(zone_id, x+dx, y+dy) for dx, dy in [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1)
        ]
    ]
