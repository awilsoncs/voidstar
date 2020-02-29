from components import Brain
from components.enums import Intention
from scenes.start_menu import get_start_menu
from systems.utilities import retract_intention


def run(scene):
    quitters = [b for b in scene.cm.get(Brain) if b.intention is Intention.QUIT_GAME]
    if quitters:
        for brain in quitters:
            retract_intention(scene, brain.entity)
        scene.controller.push_scene(get_start_menu())

