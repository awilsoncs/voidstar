from components import Coordinates, Appearance
from components.animation_effects.float import AnimationFloat
from engine import core, palettes
from engine.base_components.entity import Entity
from engine.constants import PRIORITY_HIGH


def floaty_animation(x, y, symbol, color, name):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name=name),
            Appearance(
                entity=entity_id,
                symbol=symbol,
                color=color,
                bg_color=palettes.BACKGROUND,
                render_mode=Appearance.RenderMode.HIGH_VEE
            ),
            Coordinates(entity=entity_id, x=x, y=y, priority=PRIORITY_HIGH, buildable=True),
            AnimationFloat(entity=entity_id, duration=5),
        ]
    )


def confused_animation(x, y):
    return floaty_animation(x, y, '?', palettes.LIGHT_WATER, 'confused_animation')


def no_money_animation(x, y):
    return floaty_animation(x, y, '$', palettes.FRESH_BLOOD, 'no_money_animation')


def help_animation(x, y):
    return floaty_animation(x, y, '!', palettes.FRESH_BLOOD, 'help_animation')


def knockback_animation(x, y):
    return floaty_animation(x, y, '*', palettes.GOLD, 'knockback_animation')


def sleep_animation(x, y):
    return floaty_animation(x, y, 'z', palettes.LIGHT_WATER, 'sleep_animation')
