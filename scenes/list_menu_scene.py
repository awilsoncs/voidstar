from collections import namedtuple

import tcod.console
import tcod.event

import settings
from engine import GameScene, core, palettes

MenuAction = namedtuple(
    'MenuAction',
    [
        'key',
        'verb',
        'callback'
    ]
)


class ListMenuScene(GameScene):
    def __init__(
            self,
            title,
            items,
            row_builder,
            default_action,
            menu_actions: dict = None,
            id_extractor=lambda x: x.id,
            close_after_action=False,
            parent_scene=None
    ):
        super().__init__()
        self.title = title
        self.items = items  # a query
        self.row_builder = row_builder  # fn:item -> list[str]
        self.default_action = default_action
        self.menu_actions = menu_actions if menu_actions else {}
        self.selected_line = 0
        self.id_extractor = id_extractor
        self.close_after_action = close_after_action  # if True, pop the scene after taking any action
        self.parent_scene = parent_scene

    def update(self):
        key_event = core.wait_for_char()
        if key_event:
            key_event = key_event.sym
        if key_event == tcod.event.K_DOWN:
            self.selected_line += 1
        elif key_event == tcod.event.K_UP:
            self.selected_line -= 1
        elif key_event in self.menu_actions.keys():
            self.menu_actions[key_event].callback(
                self.id_extractor(
                    self.items()[self.selected_line]
                )
            )
            if self.close_after_action:
                self.controller.pop_scene()
        elif key_event is tcod.event.K_ESCAPE:
            self.controller.pop_scene()
        elif key_event is tcod.event.K_RETURN:
            self.default_action.callback(
                self.id_extractor(
                    self.items()[self.selected_line]
                )
            )
            if self.close_after_action:
                self.controller.pop_scene()
        self.parent_scene.update()

    def render(self):
        self.gui.root.clear()
        window = self.gui.root
        window.draw_rect(
            0, 0,
            settings.SCREEN_WIDTH,
            settings.SCREEN_HEIGHT,
            0,
            fg=palettes.WHITE,
            bg=palettes.BACKGROUND
        )
        window.print(0, 0, self.title)
        window.print(0, 1, '    '.join(
            [f'({a.key}) {a.verb}' for a in self.menu_actions.values()]
        ))
        for row, item in enumerate(self.items(), 2):
            if self.selected_line + 2 == row:
                window.draw_rect(
                    0, row,
                    settings.SCREEN_WIDTH,
                    1,
                    0,
                    fg=palettes.BACKGROUND,
                    bg=palettes.WHITE
                )
                self.print(window, 4, row, item, fg=palettes.BACKGROUND, bg=palettes.WHITE)
            else:
                self.print(window, 4, row, item)

    def print(self, window, x, y, item, fg=palettes.WHITE, bg=palettes.BACKGROUND):
        window.print(
            x, y,
            ' - '.join(self.row_builder(item)),
            fg=fg, bg=bg
        )

    def register_action(self, key_event, char, text, callback):
        self.menu_actions[key_event] = MenuAction(char, text, callback)
