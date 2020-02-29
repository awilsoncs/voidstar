from engine.component_manager import ComponentManager
from gui.gui import Gui
from gui.gui_element import GuiElement
from gui.popup_message import PopupMessage


class GameScene:
    """Provide the controller behavior of the SceneController."""

    def __init__(self, debug=False):
        self.gui_elements = []
        self.cm: ComponentManager = None
        self.controller = None
        self.gui = None
        self.debug = debug

    def add_gui_element(self, element: GuiElement):
        if element.single_shot:
            # if it's a single shot (menu or popup message), we need to render it directly to the existing window
            element.render_to_screen(self.gui.root)
        else:
            self.gui_elements.append(element)

    def popup_message(self, message: str):
        self.add_gui_element(PopupMessage(message))

    # Scene Lifecycle Hooks
    # - on_load
    #   - before_update
    #   - update
    #   - render
    # - on_unload
    def on_load(self):
        pass

    def before_update(self):
        pass

    def update(self):
        """Perform the game scene behavior and set the next scene to be executed."""
        pass

    def render(self):
        self.gui.erase()
        for element in self.gui_elements:
            element.render_to_screen(self.gui.root)

    def on_unload(self):
        pass

    def prepare(
        self,
        controller: 'GameSceneController',
        cm: ComponentManager,
        gui: Gui
    ):
        self.controller = controller
        self.cm = cm
        self.gui = gui

    def pop(self):
        self.controller.pop_scene()
