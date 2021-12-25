from components import Entity, Coordinates, Appearance
from components.animation_effects.float import AnimationFloat
from engine import core, palettes
from engine.constants import PRIORITY_HIGH


def confused_animation(x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='confused_anim'),
            Appearance(entity=entity_id, symbol='?', color=palettes.LIGHT_WATER, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_HIGH, buildable=True),
            AnimationFloat(entity=entity_id, duration=5),
        ]
    )


def no_money_animation(x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='no_money_anim'),
            Appearance(entity=entity_id, symbol='$', color=palettes.FRESH_BLOOD, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_HIGH, buildable=True),
            AnimationFloat(entity=entity_id, duration=5),
        ]
    )


def help_animation(x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='help_anim'),
            Appearance(entity=entity_id, symbol='!', color=palettes.HORDELING, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_HIGH, buildable=True),
            AnimationFloat(entity=entity_id, duration=5),
        ]
    )


def knockback_animation(x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='knockback_anim'),
            Appearance(entity=entity_id, symbol='x', color=palettes.GOLD, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_HIGH, buildable=True),
            AnimationFloat(entity=entity_id, duration=5),
        ]
    )


def cant_shoot_animation(x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='cant_shoot_anim'),
            Appearance(entity=entity_id, symbol=')', color=palettes.LIGHT_WATER, bg_color=palettes.BACKGROUND),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_HIGH, buildable=True),
            AnimationFloat(entity=entity_id, duration=5),
        ]
    )
