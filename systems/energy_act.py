from components import TimedActor
from engine import core


def run(scene) -> None:
    for actor in get_actors(scene):
        actor.act(scene)
        actor.next_update = core.time_ms() + actor.timer_delay


def get_actors(scene):
    return [
        actor
        for actor in scene.cm.get(TimedActor)
        if actor.energy >= 0
    ]
