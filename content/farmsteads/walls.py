from components import Appearance, Coordinates, Attributes
from components.death_listeners.npc_corpse import Corpse
from components.death_listeners.schedule_rebuild import ScheduleRebuild
from components.faction import Faction
from components.material import Material
from components.relationships.owner import Owner
from components.structure import Structure
from components.pathfinder_cost import PathfinderCost
from engine import core, palettes, types
from engine.base_components.entity import Entity
from engine.constants import PRIORITY_MEDIUM
from engine.types import EntityId

description = "A wall, made of a light, grassy material. Be wary, it's highly flammable."


def make_wall(root_id, x, y, piece='um') -> types.Entity:
    entity_id: EntityId = core.get_id()
    glyph = piece_map[piece]

    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='wall'),
            Owner(entity=entity_id, owner=root_id),
            Appearance(entity=entity_id, symbol=glyph, color=palettes.STRAW, bg_color=palettes.BACKGROUND),
            Corpse(entity=entity_id, symbol='%', color=palettes.STRAW, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_MEDIUM),
            Attributes(entity=entity_id, hp=80, max_hp=80),
            Faction(entity=entity_id, faction=Faction.Options.PEASANT),
            Material(entity=entity_id, blocks=True, blocks_sight=True),
            ScheduleRebuild(entity=entity_id, root=root_id),
            PathfinderCost(entity=entity_id, cost=10),
            Structure(entity=entity_id)
        ]
    )


piece_map = {
    'ul': '╔',
    'um': '═',
    'ur': '╗',
    'ml': '║',
    'br': '╝',
    'bm': '═',
    'bl': '╚',
    'mr': '║'
}