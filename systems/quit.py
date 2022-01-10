import logging

import settings
from components.actors.actor import Actor
from components.enums import Intention
from components.serialization.save_game import SaveGame
from scenes.start_menu import get_start_menu


def run(scene):
    quitters = [b for b in scene.cm.get(Actor) if b.intention is Intention.BACK]
    if quitters:
        if settings.AUTOSAVE:
            SaveGame().act(scene)
        scene.pop()
        scene.controller.push_scene(get_start_menu())

