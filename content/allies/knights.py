from components import Coordinates, Appearance, Attributes
from components.sellable import Sellable
from components.attacks.standard_attack import StandardAttack
from components.brains.stationary_attack_actor import StationaryAttackActor
from components.death_listeners.npc_corpse import Corpse
from components.faction import Faction
from components.material import Material
from components.pathfinding.normal_cost_mapper import NormalCostMapper
from components.pathfinder_cost import PathfinderCost
from components.pathfinding.target_evaluation.ally_target_evaluator import AllyTargetEvaluator
from components.tax_value import TaxValue
from engine import core, palettes
from components.base_components.entity import Entity
from engine.constants import PRIORITY_MEDIUM


def make_knight(x, y):
    entity_id = core.get_id()

    components = [
        Entity(id=entity_id, entity=entity_id, name='knight'),
        Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_MEDIUM),
        Faction(entity=entity_id, faction=Faction.Options.PEASANT),
        Corpse(entity=entity_id),
        StationaryAttackActor(entity=entity_id, root_x=x, root_y=y),
        NormalCostMapper(entity=entity_id),
        Appearance(entity=entity_id, symbol='K', color=palettes.STONE, bg_color=palettes.BACKGROUND),
        Attributes(entity=entity_id, hp=10, max_hp=10),
        StandardAttack(entity=entity_id, damage=3),
        Material(entity=entity_id, blocks=False, blocks_sight=False),
        PathfinderCost(entity=entity_id, cost=40),
        Sellable(entity=entity_id, value=0),
        AllyTargetEvaluator(entity=entity_id),
        TaxValue(entity=entity_id, value=TaxValue.KNIGHT)
    ]

    return entity_id, components
