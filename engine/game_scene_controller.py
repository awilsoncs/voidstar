import tcod

import settings
from engine import GameScene
from engine.component_manager import ComponentManager
from gui.gui import Gui


class GameSceneController:
    """FSM Controller object for the game."""

    def __init__(self, title: str):
        self.title: str = title
        self.gui: Gui = None
        self.cm = ComponentManager()
        self._scene_stack: list = []

    def push_scene(self, scene: GameScene):
        scene.prepare(self, self.cm, self.gui)
        scene.on_load()
        for gui_element in scene.gui_elements:
            gui_element.on_load()
        self._scene_stack.append(scene)

    def pop_scene(self):
        scene = self._scene_stack.pop()
        scene.on_unload()
        return scene

    def reload(self):
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
