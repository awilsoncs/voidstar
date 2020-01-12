import tcod.event

import settings
from engine import GameScene, core
from engine.palettes import Palette


class PaletteTestScene(GameScene):
    """Scene for testing height map functionality."""

    def __init__(self):
        super().__init__()
        self.height = settings.MAP_HEIGHT
        self.width = settings.MAP_WIDTH
        self.palette = Palette().get_display_list()
        self.update_screen = True

    def on_load(self):
        self.render()

    def update(self):
        key_event = core.wait_for_char()
        if key_event.sym == tcod.event.K_SPACE:
            self.reset()
        elif key_event.sym == tcod.event.K_ESCAPE:
            self.controller.pop_scene()

    def reset(self):
        self.palette = Palette().get_display_list()
        print(self.palette)

    def render(self):
        self.gui.root.clear()
        window = self.gui.root
        palette_steps = len(self.palette)
        step_width = self.width // palette_steps
        for x in range(self.width):
            palette_step = x // step_width
            if palette_step >= palette_steps:
                color = self.palette[-1]
            else:
                color = self.palette[palette_step]
            for y in range(self.height):
                window.tiles[x, y] = (
                    ord(' '),
                    (*color, 255),
                    (*color, 255)
                )