import random
from itertools import product

import numpy as np
import tcod
from tcod import console

import settings
from components import Coordinates, Appearance
from engine import palettes
from engine.component_manager import ComponentManager
from engine.core import timed
from gui.gui_element import GuiElement
from settings import MAP_FRAME_HEIGHT, MAP_FRAME_WIDTH


class PlayWindow(GuiElement):
    def __init__(
        self,
        x: int, y: int,
        width: int, height: int,
        component_manager: ComponentManager,
        visibility_map: np.array,
        memory_map: np.array
    ):
        """
        :param x: horizontal starting position of the PlayWindow
        :param y: vertical starting position of the PlayWindow
        :param width: horizontal expanse of the PlayWindow in tiles
        :param height: vertical expanse of the PlayWindow in tiles
        :param component_manager: a reference to the game's ComponentManager
        :param visibility_map: a boolean array indicating whether a tile is visible or not
        :param memory_map: a boolean array indicating whether a tile has ever been visible or not
        """
        super().__init__(x, y)
        self.cm = component_manager
        self.memory_map = memory_map
        self.visibility_map = visibility_map
        self.width = width
        self.height = height
        self.snowy = set()

        # store a console with the static terrain on it so that we don't have to regenerate it each frame
        self.memory_console = tcod.console.Console(width, height, order='F')

        # hold terrain view
        self.terrain_console = tcod.console.Console(width, height, order='F')
        self.shadow_terrain_console = tcod.console.Console(width, height, order='F')

        self.black = tcod.console.Console(width, height, order='F')
        self.console = tcod.console.Console(width, height, order='F')  # buffer console

    def on_load(self) -> None:
        self.regenerate_grass()

    @timed(25, __name__)
    def render(self, panel: console.Console) -> None:
        self.console.clear()
        self.memory_console.clear()
        self.shadow_terrain_console.blit(self.memory_console)
        self.terrain_console.blit(self.console)

        coordinates = self.cm.get(Coordinates)
        coordinates = [c for c in coordinates]
        coordinates = sorted(coordinates, key=lambda c: c.priority)
        for coord in coordinates:
            appearance = self.cm.get_one(Appearance, entity=coord.entity)
            if appearance:
                appearance_tile = appearance.to_tile()
                if appearance.render_mode == Appearance.RenderMode.NORMAL:
                    hidden_tile = (
                        appearance_tile[0],
                        (*palettes.SHADOW, 255),
                        (*palettes.BACKGROUND, 255)
                    )

                    self.console.rgba[coord.x, coord.y] = appearance_tile
                    self.memory_console.rgba[coord.x, coord.y] = hidden_tile
                elif appearance.render_mode == Appearance.RenderMode.STEALTHY:
                    self.console.rgba[coord.x, coord.y] = appearance_tile
                elif appearance.render_mode == Appearance.RenderMode.HIGH_VEE:
                    color = appearance.color
                    hidden_tile = (
                        appearance_tile[0],
                        (*color, 255),
                        (*palettes.BACKGROUND, 255)
                    )

                    self.console.rgba[coord.x, coord.y] = appearance_tile
                    self.memory_console.rgba[coord.x, coord.y] = hidden_tile
                else:
                    raise ValueError(f"Unrecognized render mode {appearance.render_mode}")

        buffer = np.where(
            self.visibility_map,
            self.console.rgba,
            self.memory_console.rgba
        )
        self.console = tcod.console.Console(self.width, self.height, order='F', buffer=buffer)
        self.console.blit(panel, dest_x=self.x, dest_y=self.y, width=self.width, height=self.height)

    def regenerate_grass(self):
        memory_color = palettes.SHADOW
        for y in range(MAP_FRAME_HEIGHT):
            for x in range(MAP_FRAME_WIDTH):
                grass_color = palettes.GRASS

                if random.random() < settings.GRASS_DENSITY:
                    symbol = ord(random.choice(['.', ',', '"', '\'']))
                else:
                    symbol = ord(' ')

                self.terrain_console.tiles[x, y] = (
                    symbol,
                    (*grass_color, 255),
                    (*palettes.BACKGROUND, 255)
                )
                self.shadow_terrain_console.tiles[x, y] = (
                    symbol,
                    (*memory_color, 255),
                    (*palettes.BACKGROUND, 255)
                )

    def add_snow(self):
        all_tiles = set(product(range(1, settings.MAP_FRAME_WIDTH - 1), range(1, settings.MAP_FRAME_HEIGHT - 1)))
        unsnowed = all_tiles - self.snowy
        if not unsnowed:
            return
        x, y = random.choice(list(unsnowed))

        if random.random() < settings.GRASS_DENSITY / 2:
            symbol = ord(random.choice(['.', ',', '"', '\'']))
        else:
            symbol = ord(' ')

        self.terrain_console.tiles[x, y] = (
            symbol,
            (*palettes.WHITE, 255),
            (*palettes.BACKGROUND, 255)
        )

        self.shadow_terrain_console.tiles[x, y] = (
            symbol,
            (*palettes.SHADOW, 255),
            (*palettes.BACKGROUND, 255)
        )
        self.snowy.add((x, y))

    def add_grass(self):
        if not self.snowy:
            return

        snowy_tiles = list(self.snowy)
        x, y = random.choice(snowy_tiles)
        self.snowy.remove((x, y))

        if random.random() < settings.GRASS_DENSITY:
            symbol = ord(random.choice(['.', ',', '"', '\'']))
        else:
            symbol = ord(' ')

        self.terrain_console.tiles[x, y] = (
            symbol,
            (*palettes.GRASS, 255),
            (*palettes.BACKGROUND, 255)
        )

        self.shadow_terrain_console.tiles[x, y] = (
            symbol,
            (*palettes.SHADOW, 255),
            (*palettes.BACKGROUND, 255)
        )



