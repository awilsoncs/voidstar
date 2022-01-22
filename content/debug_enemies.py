from components import Appearance, Attributes, Coordinates
from components.attacks.attack import Attack
from components.base_components.entity import Entity
from components.death_listeners.npc_corpse import Corpse
from components.death_listeners.drop_gold import DropGold
from components.faction import Faction
from components.material import Material
from components.tags.hordeling_tag import HordelingTag
from engine import core, palettes
from engine.constants import PRIORITY_MEDIUM


def make_debug_hordeling(x, y):
    entity_id = core.get_id()

    components = [
        Entity(id=entity_id, entity=entity_id, name='debug_hordeling'),
        Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_MEDIUM),
        Faction(entity=entity_id, faction=Faction.Options.MONSTER),
        Corpse(entity=entity_id),
        Appearance(entity=entity_id, symbol='h', color=palettes.HORDELING, bg_color=palettes.BACKGROUND),
        Attributes(entity=entity_id, hp=1, max_hp=1),
        Attack(entity=entity_id, damage=1),
        Material(entity=entity_id, blocks=True, blocks_sight=False),
        HordelingTag(entity=entity_id),
        DropGold(entity=entity_id)
    ]

    return (
        entity_id,
        components
    )
