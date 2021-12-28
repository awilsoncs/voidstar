from typing import List

from components import Entity, Appearance, Attributes, Coordinates
from components.brains.peasant_actor import PeasantActor
from components.death_listeners.npc_corpse import Corpse
from components.cry_for_help import CryForHelp
from components.faction import Faction
from components.material import Material
from components.move import Move
from components.relationships.residence import Residence
from components.tags.peasant_tag import PeasantTag
from components.target_value import PEASANT, TargetValue
from engine import core, palettes
from engine.component import Component
from engine.constants import PRIORITY_MEDIUM
from engine.types import EntityId

peasant_description = "A peasant, tasked with working the fields. " \
                      "Unaware of your incompetency, their face belies a cheerful contentment."


def make_peasant(house_id, x, y) -> Entity:
    entity_id: EntityId = core.get_id()
    components: List[Component] = [
        Entity(
            id=entity_id,
            entity=entity_id,
            name='peasant',
            description=peasant_description
        ),
        Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_MEDIUM),
        Faction(entity=entity_id, faction=Faction.Options.PEASANT),
        PeasantTag(entity=entity_id),
        Appearance(entity=entity_id, symbol='p', color=palettes.WHITE, bg_color=palettes.BACKGROUND),
        Corpse(entity=entity_id),
        Attributes(entity=entity_id, hp=10, max_hp=10),
        TargetValue(entity=entity_id, value=PEASANT),
        Material(entity=entity_id, blocks=False, blocks_sight=False),
        CryForHelp(entity=entity_id),
        Residence(entity=entity_id, house_id=house_id),
        Move(entity=entity_id),
        PeasantActor(entity=entity_id)
    ]
    return entity_id, components
