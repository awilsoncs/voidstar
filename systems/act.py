from components import Brain
from components.events.turn_event import TurnEvent


def run(scene) -> None:
    for brain in get_brains(scene):
        brain.act(scene)


def get_brains(scene):
    return [
        brain
        for brain in scene.cm.get(Brain)
        for turn in [scene.cm.get_one(TurnEvent, entity=brain.entity)]
        if turn
    ]
