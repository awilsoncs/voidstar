from components import Entity, Appearance, Senses, Brain, Attributes
from components.attack import Attack
from components.enums import ControlMode
from components.faction import Faction
from components.material import Material
from components.target_value import PLAYER, TargetValue
from engine import colors, PLAYER_ID, palettes


def make_player(zone_id):
    entity_id = PLAYER_ID

    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='player', zone=zone_id),
            Appearance(entity=entity_id, symbol='@', color=palettes.WHITE, bg_color=palettes.BACKGROUND),
            Senses(entity=entity_id, sight_radius=-1),
            Brain(entity=entity_id, control_mode=ControlMode.PLAYER, take_turn=True),
            Attributes(entity=entity_id, hp=60, max_hp=60),
            Attack(entity=entity_id, damage='1d10'),
            TargetValue(entity=entity_id, value=PLAYER),
            Faction(entity=entity_id, faction=Faction.Options.PEASANT),
            Material(entity=entity_id, blocks=True, blocks_sight=False)
        ]
    )
