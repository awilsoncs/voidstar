from components import Entity, Appearance
from components.material import Material
from engine import core, palettes


def make_tree(zone_id):
    entity_id = core.get_id()
    tree_color = palettes.FOILAGE_B
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='tree', static=True, zone=zone_id),
            Appearance(entity=entity_id, symbol='♣', color=tree_color, bg_color=palettes.BACKGROUND),
            Material(entity=entity_id, blocks=True, blocks_sight=True)
        ]
    )


def make_water(zone_id):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='tree', static=True, zone=zone_id),
            Appearance(entity=entity_id, symbol='~', color=palettes.LIGHT_WATER, bg_color=palettes.BACKGROUND),
            Material(entity=entity_id, blocks=True, blocks_sight=False)
        ]
    )
