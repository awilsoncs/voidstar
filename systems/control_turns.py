from components import Brain
from components.events.turn_event import TurnEvent
from engine.core import log_debug


def run(scene):
    turns = scene.cm.get(TurnEvent)
    # if we don't have any brains that need to take turns,
    if not turns:
        brains = scene.cm.get(Brain)
        if brains:
            scene.cm.add(*get_turns(brains))


@log_debug(__name__)
def reset_turns(scene):
    brains = scene.cm.get(Brain)
    scene.cm.add(*get_turns(brains))


def get_turns(brains):
    return [TurnEvent(entity=b.entity) for b in brains]
