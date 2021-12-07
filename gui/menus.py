import textwrap

import tcod
import tcod.event

import settings
from engine import core, palettes
from gui.gui_element import GuiElement


class Menu(GuiElement):
    """Defines a multiple choice menu within the game."""

    def __init__(self, header, options, width, callback):
        super().__init__(0, 0, single_shot=True)
        self.header = header
        self.options = options
        self.width = width
        self.callback = callback
        self.pages = [options[i:i + 10] for i in range(0, len(options), 10)]
        if len(self.pages) == 0:
            self.pages.append([])

    def render(self, panel):
        """Draw a menu to the screen and return the user's option."""
        page = 0
        index = None
        while not index:
            has_next = page + 1 < len(self.pages)
            has_previous = page > 0
            key_event = self.show_and_get_input(panel, self.pages[page], has_next=has_next, has_previous=has_previous)
            key_sym = key_event.sym
            if (
                    key_sym is tcod.event.K_RIGHT
                    or key_sym is tcod.event.K_n
            ) and has_next:
                page += 1
            elif (
                    key_sym is tcod.event.K_LEFT
                    or key_sym is tcod.event.K_p
            ) and has_previous:
                page -= 1
            elif key_sym is tcod.event.K_RETURN:
                return
            else:
                index = key_sym - ord('a')

                # adjust index for the correct page
                index += page * 10

                if 0 <= index < len(self.options) and self.callback:
                    self.callback(index)
                    return
                if self.callback:
                    self.callback(None)

    def show_and_get_input(self, root, options, has_next=False, has_previous=False):
        lines = [
            '\n'.join(
                textwrap.wrap(line, self.width, break_long_words=False, replace_whitespace=False)
            ) for line in self.header.splitlines() if line.strip() != ''
        ]
        header_height = len(lines)

        if self.header == '':
            header_height = 0
        height = len(options) + header_height
        if has_next:
            height += 1
        if has_previous:
            height += 1
        window = tcod.console.Console(self.width, height, order='F')
        window.draw_rect(0, 0, self.width, height, 0, fg=palettes.WHITE, bg=None)
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

        x = settings.SCREEN_WIDTH // 2 - self.width // 2
        y = settings.SCREEN_HEIGHT // 2 - height // 2
        window.blit(root, x, y, width=self.width, height=height)
        tcod.console_flush()

        key_event = core.wait_for_char()
        return key_event
