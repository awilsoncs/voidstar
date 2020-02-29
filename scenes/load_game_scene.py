import glob
import os

from components import Coordinates
from engine import GameScene
from gui.easy_menu import EasyMenu
from scenes.defend_scene import DefendScene


class LoadGameScene(GameScene):
    """Generate a player and a world model."""
    def __init__(self):
        super().__init__()

    def update(self):
        """Show the game's title and start menu."""

        world_files = glob.glob('./*.world')
        world_files = [str(os.path.splitext(os.path.basename(f))[0]) for f in world_files]
        world_files = [f.replace('-', ' ').title() for f in world_files]

        # show options and wait for the player's choice
        self.add_gui_element(
            EasyMenu(
                'Load which world? (ESC to go back)',
                {world_file: self._start_menu_callback(world_file) for world_file in world_files},
                48,
            )
        )

    def _start_menu_callback(self, world_file):
        def out_fn():
            self.cm.connect(world_file)
            current_zone = self.cm.get_one(Coordinates, entity=0).zone
            self.controller.pop_scene()
            self.controller.push_scene(DefendScene(current_zone))
        return out_fn
