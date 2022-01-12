import settings
from components import Entity, Appearance, Senses, Attributes, Coordinates
from components.abilities.build_fence_ability import BuildFenceAbility
from components.abilities.build_wall_ability import BuildWallAbility
from components.abilities.debug_ability import DebugAbility
from components.abilities.dig_hole_ability import DigHoleAbility
from components.abilities.fast_forward_ability import FastForwardAbility
from components.abilities.hire_knight_ability import HireKnightAbility
from components.abilities.look_ability import LookAbility
from components.abilities.place_cow_ability import PlaceCowAbility
from components.abilities.place_haunch_ability import PlaceHaunchAbility
from components.abilities.plant_sapling_ability import PlantSaplingAbility
from components.abilities.sell_ability import SellAbility
from components.abilities.shoot_ability import ShootAbility
from components.abilities.thwack_ability import ThwackAbility
from components.ability_tracker import AbilityTracker
from components.attacks.standard_attack import StandardAttack
from components.death_listeners.player_corpse import PlayerCorpse
from components.move_listeners.update_senses_on_move import UpdateSenses
from components.options import Options
from components.brains.player_actor import PlayerBrain
from components.faction import Faction
from components.material import Material
from components.move import Move
from components.season_reset_listeners.move_player_to_town_center import MovePlayerToTownCenter
from components.season_reset_listeners.save_on_season import SaveOnSeasonReset
from components.step_listeners.pickup_gold import PickupGoldOnStep
from components.target_value import PLAYER, TargetValue
from components.world_beauty import WorldBeauty
from engine import PLAYER_ID, palettes


def make_player(x, y):
    entity_id = PLAYER_ID

    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name=settings.CHARACTER_NAME),
            Coordinates(entity=entity_id, x=x, y=y),
            Appearance(entity=entity_id, symbol='@', color=palettes.WHITE, bg_color=palettes.BACKGROUND),
            PlayerCorpse(entity=entity_id),
            Senses(entity=entity_id, sight_radius=settings.TORCH_RADIUS),
            PlayerBrain(entity=entity_id),
            Attributes(entity=entity_id, hp=5, max_hp=5),
            StandardAttack(entity=entity_id, damage=1),
            TargetValue(entity=entity_id, value=PLAYER),
            Faction(entity=entity_id, faction=Faction.Options.PEASANT),
            Material(entity=entity_id, blocks=True, blocks_sight=False),
            Move(entity=entity_id),
            Options(entity=entity_id),
            MovePlayerToTownCenter(entity=entity_id),
            UpdateSenses(entity=entity_id),
            # Abilities
            AbilityTracker(entity=entity_id),
            ThwackAbility(entity=entity_id, count=3, max=3),
            ShootAbility(entity=entity_id),
            DebugAbility(entity=entity_id),
            FastForwardAbility(entity=entity_id),
            PlantSaplingAbility(entity=entity_id),
            DigHoleAbility(entity=entity_id),
            LookAbility(entity=entity_id),
            BuildWallAbility(entity=entity_id),
            BuildFenceAbility(entity=entity_id),
            SellAbility(entity=entity_id),
            PlaceCowAbility(entity=entity_id),
            HireKnightAbility(entity=entity_id),
            PlaceHaunchAbility(entity=entity_id),
            SaveOnSeasonReset(entity=entity_id),
            WorldBeauty(entity=entity_id),
            PickupGoldOnStep(entity=entity_id)
        ]
    )
