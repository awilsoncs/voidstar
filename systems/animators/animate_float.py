import random

import settings
from components import Coordinates
from components.animation_effects.float import AnimationFloat
from engine import core


def update_animation(scene, animation):
    entity = animation.entity
    coords = scene.cm.get_one(Coordinates, entity=entity)
    coords.x += random.randint(0, 1)
    coords.y -= random.randint(0, 1)

    if coords.x >= settings.MAP_WIDTH - 2 or coords.y <= 0:
        scene.cm.delete(entity)


def run(scene):
    animations = scene.cm.get(AnimationFloat)
    for animation in animations:
        if core.time_ms() > animation.next_update_time:
            update_animation(scene, animation)
            animation.next_update_time = core.time_ms() + animation.delay_ms
            animation.duration -= 1
    for animation in [a for a in scene.cm.get(AnimationFloat) if a.duration < 0]:
        scene.cm.delete(animation.entity)
