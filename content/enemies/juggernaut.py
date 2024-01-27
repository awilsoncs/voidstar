import random
from components import Appearance, Attributes, Coordinates
from engine.components.energy_actor import EnergyActor
from components.brains.default_active_actor import DefaultActiveActor
from components.attacks.attack_effects.knockback_attack import KnockbackAttack
from components.attacks.siege_attack import SiegeAttack
from components.death_listeners.npc_corpse import Corpse
from components.death_listeners.drop_gold import DropGold
from components.faction import Faction
from components.material import Material
from components.movement.move import Move
from components.pathfinding.juggernaut_cost_mapper import StraightLineCostMapper
from components.pathfinding.target_evaluation.hordeling_target_evaluator import HordelingTargetEvaluator
from components.tags.hordeling_tag import HordelingTag
from components.pathfinder_cost import PathfinderCost
from engine import core, palettes
from engine.components.entity import Entity
from engine.constants import PRIORITY_MEDIUM


def make_juggernaut(x, y):
    entity_id = core.get_id()

    components = [
        Entity(id=entity_id, entity=entity_id, name='Juggernaut'),
        Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_MEDIUM),
        Faction(entity=entity_id, faction=Faction.Options.MONSTER),
        Corpse(entity=entity_id),
        DefaultActiveActor(entity=entity_id),
        StraightLineCostMapper(entity=entity_id),
        Appearance(entity=entity_id, symbol='H', color=palettes.HORDELING, bg_color=palettes.BACKGROUND),
        Attributes(entity=entity_id, hp=3, max_hp=3),
        SiegeAttack(entity=entity_id, damage=2),
        Material(entity=entity_id, blocks=True, blocks_sight=False),
        HordelingTag(entity=entity_id),
        Move(entity=entity_id, energy_cost=EnergyActor.VERY_SLOW),
        KnockbackAttack(entity=entity_id),
        PathfinderCost(entity=entity_id, cost=5),
        HordelingTargetEvaluator(entity=entity_id)
    ]

    if random.randint(1, 10) == 10:
        components.append(DropGold(entity=entity_id))

    return (
        entity_id,
        components
    )
