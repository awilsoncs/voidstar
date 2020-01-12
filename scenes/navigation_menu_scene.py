from collections import OrderedDict

import settings
from engine import GameScene
from engine import colors
from gui.labels import Label
from gui.menus import Menu


class NavigationMenuScene(GameScene):
    """Show a menu with links to other scenes."""

    def __init__(
            self,
            title: str,
            option_scene_map: OrderedDict
    ):
        super().__init__()
        self.option_scene_map = option_scene_map
        self.options = list(self.option_scene_map.keys())
        center_x = (settings.SCREEN_WIDTH - len(title)) // 2
        center_y = settings.SCREEN_HEIGHT // 2 - 4
        title_label = Label(center_x, center_y, title, fg=colors.light_orange)
        self.add_gui_element(title_label)

    def before_update(self):
        # pre-render the gui elements so that they show up before menu pauses
        # execution
        self.gui = self.controller.gui
        self.render()

    def update(self):
        """Show the menu and wait for player selection."""
        self.add_gui_element(Menu('', self.options, 24, self._menu_callback))

    def _menu_callback(self, option):
        if option is not None:
            option_key = self.options[option]
            scene_to_push = self.option_scene_map[option_key]
            self.controller.push_scene(scene_to_push)
