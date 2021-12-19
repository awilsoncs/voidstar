from components import Entity, Appearance, Attributes, Coordinates
from components.actors.peasant_actor import PeasantActor
from components.death_listeners.npc_corpse import Corpse
from components.cry_for_help import CryForHelp
from components.faction import Faction
from components.material import Material
from components.move import Move
from components.relationships.residence import Residence
from components.tags.peasant_tag import PeasantTag
from components.target_value import PEASANT, TargetValue
from engine import core, palettes
from engine.constants import PRIORITY_MEDIUM


def make_peasant(house_id, x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='peasant'),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_MEDIUM, terrain=False),
            Faction(entity=entity_id, faction=Faction.Options.PEASANT),
            PeasantTag(entity=entity_id),
            Appearance(entity=entity_id, symbol='p', color=palettes.WHITE, bg_color=palettes.BACKGROUND),
            Corpse(entity=entity_id),
            Attributes(entity=entity_id, hp=10, max_hp=10),
            TargetValue(entity=entity_id, value=PEASANT),
            Material(entity=entity_id, blocks=False, blocks_sight=False),
            CryForHelp(entity=entity_id),
            Residence(entity=entity_id, house_id=house_id),
            Move(entity=entity_id)
        ]
    )

