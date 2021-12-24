import settings
from components import Entity, Appearance, Senses, Attributes, Coordinates
from components.abilities.shoot_ability import ShootAbility
from components.abilities.thwack_ability import ThwackAbility
from components.attacks.standard_attack import StandardAttack
from components.death_listeners.player_corpse import PlayerCorpse
from components.move_listeners.update_senses_on_move import UpdateSenses
from components.options import Options
from components.player_controllers.player_actor import PlayerActor
from components.faction import Faction
from components.material import Material
from components.move import Move
from components.season_reset_listeners.move_player_to_town_center import MovePlayerToTownCenter
from components.target_value import PLAYER, TargetValue
from engine import PLAYER_ID, palettes


def make_player(x, y):
    entity_id = PLAYER_ID

    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='player'),
            Coordinates(entity=entity_id, x=x, y=y),
            Appearance(entity=entity_id, symbol='@', color=palettes.WHITE, bg_color=palettes.BACKGROUND),
            PlayerCorpse(entity=entity_id),
            Senses(entity=entity_id, sight_radius=settings.TORCH_RADIUS),
            PlayerActor(entity=entity_id),
            Attributes(entity=entity_id, hp=5, max_hp=5),
            StandardAttack(entity=entity_id, damage=1),
            TargetValue(entity=entity_id, value=PLAYER),
            Faction(entity=entity_id, faction=Faction.Options.PEASANT),
            Material(entity=entity_id, blocks=True, blocks_sight=False),
            ThwackAbility(entity=entity_id, count=3, max=3),
            ShootAbility(entity=entity_id),
            Move(entity=entity_id),
            Options(entity=entity_id),
            MovePlayerToTownCenter(entity=entity_id),
            UpdateSenses(entity=entity_id)
        ]
    )
