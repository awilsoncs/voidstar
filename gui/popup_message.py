import settings
from gui.gui_element import GuiElement
from gui.menus import Menu


class PopupMessage(GuiElement):
    def __init__(self, message):
        super().__init__(0, 0, name=message, single_shot=True)
        self.message = message
        self.menu = Menu(message, [], settings.INVENTORY_WIDTH, lambda x: x)

    def render(self, panel):
        self.menu.render(panel)
