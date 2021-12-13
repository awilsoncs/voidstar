import logging
from typing import List

import tcod

import settings
from engine import GameScene
from engine.component_manager import ComponentManager
from engine.core import timed, log_debug
from gui.gui import Gui
from scenes.defend_scene import DefendScene


class GameSceneController:
    """FSM Controller object for the game."""

    @log_debug(__name__)
    def __init__(self, title: str):
        self.title: str = title
        self.gui: Gui = Gui(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT, title=self.title)
        self.cm = ComponentManager()
        self._scene_stack: List[GameScene] = []
        logging.getLogger(__name__).debug('GameSceneController instantiated')

    @log_debug(__name__)
    def push_scene(self, scene: GameScene):
        scene.prepare(self, self.cm, self.gui)
        self.on_load(scene)
        for gui_element in scene.gui_elements:
            gui_element.on_load()
        self._scene_stack.append(scene)

    @timed(250, __name__)
    def on_load(self, scene):
        scene.on_load()

    @log_debug(__name__)
    def pop_scene(self):
        scene = self._scene_stack.pop()
        scene.on_unload()
        return scene

    @log_debug(__name__)
    def reload(self):
        logging.debug('reloading scene')
        scene = self.pop_scene()
        self.push_scene(scene)

    @log_debug(__name__)
    def clear_scenes(self):
        self._scene_stack.clear()

    @log_debug(__name__)
    def start(self):
        """Invoke the FSM execution and transition."""
        while self._scene_stack:
            self._scene_stack[-1].before_update()
            self._scene_stack[-1].update()
            if self._scene_stack:
                self._scene_stack[-1].render()
                tcod.console_flush()
