import logging
import os

import settings
from engine import GameScene, core, palettes
from engine.serialization import serialization
from gui.easy_menu import EasyMenu
from gui.labels import Label
from scenes.defend_scene import DefendScene


class LoadMenuScene(GameScene):
    """Show a menu with links to other scenes."""

    def __init__(self):
        super().__init__()
        self.title = "Load a village?"
        center_x = (settings.SCREEN_WIDTH - len(self.title)) // 2
        center_y = settings.SCREEN_HEIGHT // 2 - 4
        title_label = Label(center_x, center_y, self.title, fg=palettes.FRESH_BLOOD)
        self.add_gui_element(title_label)

    def before_update(self):
        # pre-render the gui elements so that they show up before menu pauses
        # execution
        self.gui = self.controller.gui
        self.render()

    def update(self):
        """Show the menu and wait for player selection."""
        files = []

        for file in os.listdir("."):
            if file.endswith(".world"):
                files.append(file)

        self.gui.add_element(
            EasyMenu(
                "Load which?",
                {
                    world: self.get_world_loader(world) for world in files
                },
                settings.INVENTORY_WIDTH,
            )
        )

    def get_world_loader(self, file_name):
        def out_fn():
            self.load_world(file_name)
        return out_fn

    def load_world(self, file_name):
        self.pop()
        self.controller.push_scene(DefendScene(from_file=file_name))
