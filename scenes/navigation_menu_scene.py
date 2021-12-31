from collections import OrderedDict

import settings
from engine import GameScene, palettes
from gui.easy_menu import EasyMenu
from gui.labels import Label


class NavigationMenuScene(GameScene):
    """Show a menu with links to other scenes."""

    def __init__(
            self,
            title: str,
            option_scene_map: OrderedDict
    ):
        super().__init__()
        self.options = option_scene_map
        center_x = (settings.SCREEN_WIDTH - len(title)) // 2
        center_y = settings.SCREEN_HEIGHT // 2 - 4
        title_label = Label(center_x, center_y, title, fg=palettes.FRESH_BLOOD)
        self.add_gui_element(title_label)

    def before_update(self):
        # pre-render the gui elements so that they show up before menu pauses
        # execution
        self.gui = self.controller.gui
        self.render()

    def update(self):
        """Show the menu and wait for player selection."""
        self.add_gui_element(
            EasyMenu(
                '',
                {link[0]: self.get_push_scene(link[1]) for link in self.options.items()},
                24,
                hide_background=False
            )
        )

    def get_push_scene(self, scene):
        def out_fn():
            self.controller.push_scene(scene)
        return out_fn

    def on_load(self):
        self.sound.play('theme')
