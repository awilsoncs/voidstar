import logging
from typing import List

import tcod

import settings
from engine import GameScene
from engine.component_manager import ComponentManager
from engine.core import timed, log_debug
from engine.sound.default_sound_controller import DefaultSoundController
from gui.gui import Gui


class GameSceneController:
    """FSM Controller object for the game."""

    @log_debug(__name__)
    def __init__(self, title: str):
        self.title: str = title
        self.gui: Gui = Gui(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT, title=self.title)
        self.cm = ComponentManager()
        self.sound = DefaultSoundController()
        self._scene_stack: List[GameScene] = []
        logging.getLogger(__name__).debug('GameSceneController instantiated')

    @log_debug(__name__)
    def push_scene(self, scene: GameScene):
        scene.load(self, self.cm, self.gui, self.sound)
        for gui_element in scene.gui_elements:
            gui_element.on_load()
        self._scene_stack.append(scene)

    @log_debug(__name__)
    def pop_scene(self):
        scene = self._scene_stack.pop()
        scene.on_unload()
        return scene

    @log_debug(__name__)
    def clear_scenes(self):
        self._scene_stack.clear()

    @log_debug(__name__)
    def start(self):
        """Invoke the FSM execution and transition."""
        while self._scene_stack:
            current_scene = self._scene_stack[-1]
            current_scene.before_update()
            current_scene.update()
            current_scene.render()
            tcod.console_flush()
