import settings
from components import Entity, Appearance, Senses, Attributes, Coordinates
from components.abilities.shoot_ability import ShootAbility
from components.abilities.thwack_ability import ThwackAbility
from components.actors.player_dead_actor import PlayerDeadActor
from components.attack import Attack
from components.actors.player_actor import PlayerActor
from components.corpse import Corpse
from components.enums import ControlMode
from components.faction import Faction
from components.material import Material
from components.move import Move
from components.target_value import PLAYER, TargetValue
from engine import PLAYER_ID, palettes
from engine.constants import PRIORITY_LOW


def make_player(zone_id):
    entity_id = PLAYER_ID

    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='player', zone=zone_id),
            Appearance(entity=entity_id, symbol='@', color=palettes.WHITE, bg_color=palettes.BACKGROUND),
            Corpse(entity=entity_id),
            Senses(entity=entity_id, sight_radius=settings.TORCH_RADIUS),
            PlayerActor(entity=entity_id),
            Attributes(entity=entity_id, hp=5, max_hp=5),
            Attack(entity=entity_id, damage=1),
            TargetValue(entity=entity_id, value=PLAYER),
            Faction(entity=entity_id, faction=Faction.Options.PEASANT),
            Material(entity=entity_id, blocks=True, blocks_sight=False),
            ThwackAbility(entity=entity_id, count=3, max=3),
            ShootAbility(entity=entity_id),
            Move(entity=entity_id)
        ]
    )


def make_corpse(x, y):
    entity_id = PLAYER_ID

    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='player corpse'),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOW),
            Appearance(entity=entity_id, symbol='%', color=palettes.BLOOD, bg_color=palettes.BACKGROUND),
            PlayerDeadActor(entity=entity_id),
        ]
    )
