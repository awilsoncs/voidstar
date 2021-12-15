from components import Entity, Appearance, Coordinates, Attributes
from components.death_listeners.npc_corpse import Corpse
from components.death_listeners.schedule_rebuild import ScheduleRebuild
from components.faction import Faction
from components.material import Material
from components.owner import Owner
from engine import core, palettes
from engine.constants import PRIORITY_MEDIUM


def make_wall(root_id, x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='wall'),
            Owner(entity=entity_id, owner=root_id),
            Appearance(entity=entity_id, symbol='#', color=palettes.STRAW, bg_color=palettes.BACKGROUND),
            Corpse(entity=entity_id, symbol='%', color=palettes.STRAW, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_MEDIUM),
            Attributes(entity=entity_id, hp=80, max_hp=80),
            Faction(entity=entity_id, faction=Faction.Options.PEASANT),
            Material(entity=entity_id, blocks=True, blocks_sight=True),
            ScheduleRebuild(entity=entity_id, root=root_id)
        ]
    )