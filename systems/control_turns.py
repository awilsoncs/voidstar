from components import TimedActor
from components.events.turn_event import TurnEvent
from engine.core import log_debug


def run(scene):
    turns = scene.cm.get(TurnEvent)
    # if we don't have any actors that need to take turns,
    if not turns:
        actors = scene.cm.get(TimedActor)
        if actors:
            scene.cm.add(*get_turns(actors))


@log_debug(__name__)
def reset_turns(scene):
    actors = scene.cm.get(TimedActor)
    scene.cm.add(*get_turns(actors))


def get_turns(actors):
    return [TurnEvent(entity=b.entity) for b in actors]
