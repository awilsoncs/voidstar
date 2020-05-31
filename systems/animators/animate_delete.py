from components.animation_effects.deleter import AnimationDeleter
from engine import core


def run(scene):
    deleters = scene.cm.get(AnimationDeleter)
    for deleter in deleters:
        if core.time_ms() > deleter.start + deleter.duration:
            scene.cm.delete(deleter.entity)
