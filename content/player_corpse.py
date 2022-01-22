from components import Coordinates, Appearance
from components.abilities.debug_ability import DebugAbility
from components.abilities.look_ability import LookAbility
from components.ability_tracker import AbilityTracker
from components.brains.player_dead_actor import PlayerDeadBrain
from engine import core, palettes
from components.base_components.entity import Entity
from engine.constants import PRIORITY_LOW


def make_player_corpse(x, y):
    """Create a corpse with some remaining agency."""
    entity_id = core.get_id()

    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='player corpse'),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOW),
            Appearance(entity=entity_id, symbol='%', color=palettes.BLOOD, bg_color=palettes.BACKGROUND),
            PlayerDeadBrain(entity=entity_id),
            AbilityTracker(entity=entity_id),
            DebugAbility(entity=entity_id),
            LookAbility(entity=entity_id)
        ]
    )