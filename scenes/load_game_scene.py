import glob
import os

from components import Coordinates
from engine import GameScene
from gui.menus import Menu
from scenes.simulation_scene import SimulationScene


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
            Menu(
                'Load which world? (ESC to go back)',
                world_files,
                48,
                self._start_menu_callback(world_files)
            )
        )

    def _start_menu_callback(self, world_files):
        def callback(option):
            if option is None:
                self.controller.pop_scene()
                return
            else:
                file_name = world_files[option]
                file_name = file_name.replace(' ', '-').lower()
                self.cm.connect(file_name)
                current_zone = self.cm.get_one(Coordinates, entity=0).zone
                self.controller.pop_scene()
                self.controller.push_scene(SimulationScene(current_zone))
        return callback
