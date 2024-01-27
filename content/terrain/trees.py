from components import Appearance, Coordinates, Attributes
from components.sellable import Sellable
from components.death_listeners.npc_corpse import Corpse
from components.death_listeners.terrain_changes_on_death import TerrainChangedOnDeath
from components.faction import Faction
from components.material import Material
from components.tags.tree_tag import TreeTag
from components.pathfinder_cost import PathfinderCost
from components.tree_cut_on_die import TreeCutOnDeath
from engine import core, palettes
from engine.components.entity import Entity
from engine.constants import PRIORITY_MEDIUM


wall_tree_description = "This hardy species of Toshim tree towers over the village. " \
                        "You won't be able to cut this one down."


def make_wall_tree(x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(
                id=entity_id,
                entity=entity_id,
                name='hardy tree',
                static=True,
                description=wall_tree_description
            ),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_MEDIUM),
            Appearance(entity=entity_id, symbol='♣', color=palettes.WALL_TREE, bg_color=palettes.BACKGROUND),
            Material(entity=entity_id, blocks=True, blocks_sight=True),
            PathfinderCost(entity=entity_id, cost=100)
        ]
    )


tree_description = "A tree of the Toshim Plains. You can chop it down to sell its valuable wood."


def make_tree(x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(
                id=entity_id,
                entity=entity_id,
                name='tree',
                static=True,
                description=tree_description
            ),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_MEDIUM),
            Attributes(entity=entity_id, hp=5, max_hp=5),
            Corpse(entity=entity_id, symbol="%", color=palettes.WOOD),
            Faction(entity=entity_id, faction=Faction.Options.PEASANT),
            Appearance(entity=entity_id, symbol='♣', color=palettes.FOILAGE_C, bg_color=palettes.BACKGROUND),
            Material(entity=entity_id, blocks=True, blocks_sight=True),
            TreeTag(entity=entity_id),
            TerrainChangedOnDeath(entity=entity_id),
            Sellable(entity=entity_id, value=2),
            PathfinderCost(entity=entity_id, cost=20),
            TreeCutOnDeath(entity=entity_id)
        ]
    )
