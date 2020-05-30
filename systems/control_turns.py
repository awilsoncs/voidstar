from components import Brain
from components.events.turn_event import TurnEvent


def run(scene):
    turns = scene.cm.get(TurnEvent)
    # if we don't have any brains that need to take turns,
    if not turns:
        brains = scene.cm.get(Brain)
        scene.cm.add(*get_turns(brains))


def get_turns(brains):
    return [TurnEvent(entity=b.entity) for b in brains]
