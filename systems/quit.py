from components.actors.actor import Actor
from components.enums import Intention
from scenes.start_menu import get_start_menu


def run(scene):
    quitters = [b for b in scene.cm.get(Actor) if b.intention is Intention.BACK]
    if quitters:
        for actor in quitters:
            pass
            # retract_intention(scene, actor.entity)
        scene.controller.push_scene(get_start_menu())

