from components import Brain
from components.enums import Intention
from systems.utilities import retract_intention


def run(scene):
    quitters = [b for b in scene.cm.get(Brain) if b.intention is Intention.QUIT_GAME]
    if quitters:
        for brain in quitters:
            retract_intention(scene, brain.entity)
        scene.cm.commit()
        scene.cm.close()
        scene.controller.pop_scene()
