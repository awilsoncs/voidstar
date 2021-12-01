import textwrap

import tcod
import tcod.event
from tcod.event_constants import K_RETURN

import engine
import settings
from engine import core
from engine.palettes import WHITE
from gui.gui_element import GuiElement


class EasyMenu(GuiElement):
    """Defines a multiple choice menu within the game."""

    def __init__(self, header, options, width, hide_background=True, return_only=False):
        super().__init__(0, 0, single_shot=True)
        self.header = header
        self.option_map = options
        self.options = [o for o in options.keys()]
        self.width = width
        self.pages = [self.options[i:i + 10] for i in range(0, len(self.options), 10)]
        self.hide_background = hide_background
        self.return_only = return_only
        if len(self.pages) == 0:
            self.pages.append([])

    def render(self, panel):
        """Draw a menu to the screen and return the user's option."""
        page = 0
        index = None
        while index is None:
            has_next = page + 1 < len(self.pages)
            has_previous = page > 0
            key_event = self.show_and_get_input(panel, self.pages[page], has_next=has_next, has_previous=has_previous)
            key_sym = key_event.sym
            if (key_sym is tcod.event.K_RIGHT or key_sym is tcod.event.K_n) and has_next:
                page += 1
            elif (key_sym is tcod.event.K_LEFT or key_sym is tcod.event.K_p) and has_previous:
                page -= 1
            elif key_sym is tcod.event.K_RETURN:
                return
            else:
                index = key_sym - ord('a')

                # adjust index for the correct page
                index += page * 10

                if 0 <= index < len(self.options):
                    option_at_index = self.options[index]
                    callback = self.option_map.get(
                        option_at_index,
                        lambda: print("no menu option")
                    )
                    callback()

    def show_and_get_input(self, root, options, has_next=False, has_previous=False):
        lines = textwrap.wrap(self.header, self.width, break_long_words=False, replace_whitespace=False)
        header_height = len(lines)

        if self.header == '':
            header_height = 0
        height = len(options) + header_height
        if has_next:
            height += 1
        if has_previous:
            height += 1
        window = tcod.console.Console(self.width, height, order='F')
        window.draw_rect(0, 0, self.width, height, 0, fg=WHITE, bg=None)
        for i, _ in enumerate(lines):
            window.print(1, 0 + i, lines[i])

        y = header_height
        letter_index = ord('a')
        for option_text in options:
            text = '(' + chr(letter_index) + ') ' + option_text
            window.print(0, y, text, bg=None)
            y += 1
            letter_index += 1

        # add nav
        if has_previous and not has_next:
            window.print(0, y, ' <- (p) previous', bg=None)
        elif has_next and not has_previous:
            window.print(0, y, '(n) next ->', bg=None)
        elif has_next and has_previous:
            window.print(0, y, ' <- (p) previous (n) next ->', bg=None)

        if self.hide_background:
            # Draw a blank screen
            background = tcod.console.Console(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT, order='F')
            background.draw_rect(0, 0, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT, 0, bg=engine.palettes.BACKGROUND)
            background.blit(root)

        x = settings.SCREEN_WIDTH // 2 - self.width // 2
        y = settings.SCREEN_HEIGHT // 2 - height // 2
        window.blit(root, x, y, width=self.width, height=height)

        tcod.console_flush()

        key_event = core.wait_for_char()
        if self.return_only:
            while key_event is None or int(key_event.sym) is not K_RETURN:
                key_event = core.wait_for_char()

        return key_event
