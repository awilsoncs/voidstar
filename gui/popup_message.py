from dataclasses import dataclass

import settings
from gui.easy_menu import EasyMenu
from gui.gui_element import GuiElement


@dataclass
class PopupMessage(GuiElement):

    def __init__(self, message):
        super().__init__(0, 0, name=message, single_shot=True)
        self.message = message
        self.menu = EasyMenu(message, {}, settings.INVENTORY_WIDTH)

    def render(self, panel):
        self.menu.render(panel)
