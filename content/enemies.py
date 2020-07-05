import random
from components import Entity, Appearance, Attributes, Coordinates
from components.attack import Attack
from components.actors.monster_actor import MonsterTimedActor
from components.drop_gold import DropGold
from components.enums import ControlMode
from components.faction import Faction
from components.material import Material
from components.tags import Tag
from engine import core, palettes
from engine.constants import PRIORITY_MEDIUM


def make_hordeling(x, y):
    entity_id = core.get_id()

    components = [
        Entity(id=entity_id, entity=entity_id, name='hordeling'),
        Coordinates(
            entity=entity_id,
            x=x,
            y=y,
            priority=PRIORITY_MEDIUM,
            terrain=False,
        ),
        Faction(entity=entity_id, faction=Faction.Options.MONSTER),
        MonsterTimedActor(entity=entity_id, control_mode=ControlMode.MONSTER),
        Appearance(entity=entity_id, symbol='h', color=palettes.HORDELING, bg_color=palettes.BACKGROUND),
        Attributes(entity=entity_id, hp=1, max_hp=1),
        Attack(entity=entity_id, damage='1d1'),
        Material(entity=entity_id, blocks=True, blocks_sight=False),
        Tag(entity=entity_id, value='hordeling')
    ]

    if random.randint(1, 10) == 10:
        components.append(DropGold(entity=entity_id))

    return (
        entity_id,
        components
    )
