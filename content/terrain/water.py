import random

from components import Appearance, Coordinates
from components.animation_effects.randomized_blinker import RandomizedBlinker
from components.diggable import Diggable
from components.flooder import Flooder
from components.material import Material
from components.states.move_cost_affectors import DifficultTerrain
from components.pathfinder_cost import PathfinderCost
from components.tags.ice_tag import IceTag
from components.tags.water_tag import WaterTag
from engine import core, palettes
from engine.components.entity import Entity
from engine.constants import PRIORITY_LOWEST


def make_water(x, y, rapidness=5000):
    entity_id = core.get_id()
    water_color = random.choice([palettes.LIGHT_WATER, palettes.WATER])
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='water', static=True),
            Appearance(entity=entity_id, symbol='~', color=water_color, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOWEST),
            Material(entity=entity_id, blocks=False, blocks_sight=False),
            DifficultTerrain(entity=entity_id),
            Diggable(entity=entity_id),
            Flooder(entity=entity_id),
            PathfinderCost(entity=entity_id, cost=10),
            RandomizedBlinker(
                entity=entity_id,
                new_symbol='~',
                new_color=palettes.WATER,
                new_bg_color=palettes.BACKGROUND,
                timer_delay=rapidness,
                next_update=core.time_ms()+random.randint(0, rapidness)
            ),
            WaterTag(entity=entity_id)
        ]
    )


def make_swampy_water(x, y, rapidness):
    entity_id = core.get_id()
    water_color = random.choice([palettes.GRASS, palettes.WATER])
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='swampy water', static=True),
            Appearance(entity=entity_id, symbol='~', color=water_color, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_LOWEST),
            Material(entity=entity_id, blocks=False, blocks_sight=False),
            DifficultTerrain(entity=entity_id),
            Diggable(entity=entity_id),
            Flooder(entity=entity_id),
            PathfinderCost(entity=entity_id, cost=10),
            RandomizedBlinker(
                entity=entity_id,
                new_symbol='~',
                new_color=palettes.GRASS,
                new_bg_color=palettes.BACKGROUND,
                timer_delay=rapidness*4,
                next_update=core.time_ms()+random.randint(0, rapidness*4)
            ),
            WaterTag(entity=entity_id)
        ]
    )


def freeze(scene, eid):
    entity = scene.cm.get_one(Entity, entity=eid)
    if 'swampy' in entity.name:
        entity.name = 'gross ice'
    else:
        entity.name = 'ice'

    appearance = scene.cm.get_one(Appearance, entity=eid)
    appearance.symbol = '░'

    material = scene.cm.get_one(Material, entity=eid)
    material.blocks = False

    ice_tag = IceTag(entity=eid)

    for component_type in [WaterTag, Flooder, DifficultTerrain, PathfinderCost, RandomizedBlinker]:
        component = scene.cm.get_one(component_type, entity=eid)
        ice_tag.frozen_components.append(component.id)
        scene.cm.stash_component(component.id)

    scene.cm.add(ice_tag)


def thaw(scene, eid):
    entity = scene.cm.get_one(Entity, entity=eid)
    if 'gross' in entity.name:
        entity.name = 'swampy water'
    else:
        entity.name = 'water'

    appearance = scene.cm.get_one(Appearance, entity=eid)
    appearance.symbol = '~'

    material = scene.cm.get_one(Material, entity=eid)
    material.blocks = True

    ice_tag = scene.cm.get_one(IceTag, entity=eid)

    for cid in ice_tag.frozen_components:
        scene.cm.unstash_component(cid)

    scene.cm.delete_component(ice_tag)
