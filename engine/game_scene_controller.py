import logging

import tcod

import settings
from engine import GameScene
from engine.component_manager import ComponentManager
from engine.core import time_ms, timed
from gui.gui import Gui
from scenes.defend_scene import DefendScene


class GameSceneController:
    """FSM Controller object for the game."""

    def __init__(self, title: str):
        self.title: str = title
        self.gui: Gui = None
        self.cm = ComponentManager()
        self._scene_stack: list = []
        logging.debug('GameSceneController instantiated')

    def push_scene(self, scene: GameScene):
        scene.prepare(self, self.cm, self.gui)
        self.on_load(scene)
        for gui_element in scene.gui_elements:
            gui_element.on_load()
        self._scene_stack.append(scene)

    @timed(1000)
    def on_load(self, scene):
        scene.on_load()

    def pop_scene(self):
        scene = self._scene_stack.pop()
        scene.on_unload()
        return scene

    def reload(self):
        logging.debug('reloading scene')
        scene = self.pop_scene()
        self.push_scene(scene)

    def clear_scenes(self):
        self._scene_stack.clear()

    def start(self):
        """Invoke the FSM execution and transition."""
        self.gui = Gui(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT, title=self.title)
        while self._scene_stack:
            self._scene_stack[-1].before_update()
            self._scene_stack[-1].update()
            if self._scene_stack:
                self._scene_stack[-1].render()
                tcod.console_flush()

    def next_level(self, peasants, monsters):
        self.pop_scene()

        # TODO the game scene controller shouldn't be responsible for choosing the next scene
        self.push_scene(DefendScene(peasants, monsters))
