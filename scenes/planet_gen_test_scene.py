import math
import random
from dataclasses import dataclass
from typing import Tuple

import numpy
import tcod
import tcod.event

import settings
from engine import GameScene, core, colors
from engine.palettes import Palette

RUGGEDNESS_BASE = 0.12
RUGGEDNESS_SD = 0.01


@dataclass
class PlanetTile(object):
    elevation: float = 0.0
    prevailing_wind: Tuple[float, float] = (0.0, 0.0)
    precipitation: float = 0.0
    temperature: float = 0.0
    biome: str = None

class PlanetGenTestScene(GameScene):
    """Scene for testing height map functionality."""

    def __init__(self):
        super().__init__()
        self.height = settings.MAP_HEIGHT
        self.width = settings.MAP_WIDTH
        self.layers = [1.0, 6.0, 20.0, 100.0]
        self.generators = [core.get_noise_generator(dimensions=3) for _ in range(len(self.layers))]
        self.burn = core.get_noise_generator(dimensions=3)
        self.update_screen = True
        self.map = numpy.zeros((self.width, self.height), order='F')
        self.water_level = random.uniform(0.0, 1.0)
        self.mountain_level = 0.95
        self.ruggedness = random.normalvariate(RUGGEDNESS_BASE, RUGGEDNESS_SD)
        self.freezing_zone = random.normalvariate(1.25, 0.25)
        self.tilt = random.randint(-5, 5)
        self.map_colors = Palette()

    def on_load(self):
        self.regenerate()
        self.render()

    def update(self):
        key_event = core.wait_for_char()
        if key_event.sym == tcod.event.K_SPACE:
            self.reset()
        elif key_event.sym == tcod.event.K_l:
            self.water_level += 0.01
        elif key_event.sym == tcod.event.K_k:
            self.water_level -= 0.01
        elif key_event.sym == tcod.event.K_p:
            self.mountain_level += 0.01
        elif key_event.sym == tcod.event.K_o:
            self.mountain_level -= 0.01
        elif key_event.sym == tcod.event.K_m:
            self.freezing_zone -= 0.1
        elif key_event.sym == tcod.event.K_n:
            self.freezing_zone += 0.1
        elif key_event.sym == tcod.event.K_x:
            self.ruggedness += 0.01
            print(self.ruggedness)
        elif key_event.sym == tcod.event.K_z:
            self.ruggedness -= 0.01
            print(self.ruggedness)
        elif key_event.sym == tcod.event.K_q:
            tcod.sys_save_screenshot()
        elif key_event.sym == tcod.event.K_ESCAPE:
            self.controller.pop_scene()
        self.regenerate()

    def reset(self):
        self.generators = [core.get_noise_generator() for _ in self.generators]
        self.map_colors = Palette()
        self.tilt = random.randint(-5, 5)
        self.freezing_zone = random.normalvariate(1.25, 0.25)
        self.ruggedness = random.normalvariate(RUGGEDNESS_BASE, RUGGEDNESS_SD)
        self.water_level = random.uniform(0.0, 1.0)

    def regenerate(self):
        for x in range(self.width):
            for y in range(self.height):
                self.map[x, y] = self.get_point(x, y)
        minimum = self.map.min()
        self.map -= minimum
        self.map /= self.map.max()
        self.update_screen = True

    def get_point(self, x, y):
        cylinder_x = x / settings.MAP_WIDTH
        cylinder_y = y / settings.MAP_HEIGHT

        x_in_rad = cylinder_x * 2 * math.pi
        y_in_rad = cylinder_y * math.pi
        y_sin = math.sin(y_in_rad + math.pi)

        r = 10.0
        a = r * math.sin(x_in_rad) * y_sin
        b = r * math.cos(x_in_rad) * y_sin
        c = r * math.cos(y_in_rad)

        output = 0
        base = 100.0 / (self.ruggedness * 3.0)
        for i in range(len(self.generators)):
            value = self.generators[i].get_point(
                (132+a) / self.layers[i],
                (123+b) / self.layers[i],
                (312+c) / self.layers[i]
            )
            output += base * value
            base /= (self.ruggedness * 3.0)
        return output

    def render(self):
        if self.update_screen:
            self.gui.root.clear()
            window = self.gui.root
            for index, v in numpy.ndenumerate(self.map):
                ground, rank = self.get_elevation_rank(v)
                if self.is_frozen(index):
                    color = self.map_colors.tertiary[-1]
                elif ground:
                    color = self.map_colors.primary[rank]
                else:
                    color = self.map_colors.secondary[rank]
                if not ground:
                    # water
                    sym = '≈'
                elif rank == 9:
                    sym = '▲'
                elif rank == 7:
                    sym = '∩'
                elif rank <= 6:
                    sym = random.choice(["'", ',', '.', 'ⁿ'])
                else:
                    sym = '.'
                window.tiles[index[0], index[1]] = (
                    ord(sym),
                    (*color, 255),
                    (*colors.darken(color, factor=0.8), 255)
                )
            self.update_screen = False

    def get_elevation_rank(self, value):
        if value <= self.water_level - 0.04:
            # deep water
            return 0, 0
        elif value <= self.water_level - 0.03:
            # normal water
            return 0, 1
        elif value <= self.water_level - 0.02:
            # shallow water
            return 0, 2
        elif value <= self.water_level - 0.01:
            return 0, 3
        elif value <= self.water_level:
            return 0, 4
        elif value < self.mountain_level - 0.7:
            # low lands
            return 1, 3
        elif value < self.mountain_level - 0.5:
            # low lands
            return 1, 4
        elif value < self.mountain_level - 0.3:
            # low lands
            return 1, 5
        elif value < self.mountain_level - 0.1:
            # midlands
            return 1, 6
        elif value < self.mountain_level:
            # highlands
            return 1, 7
        else:
            # mountain
            return 1, 9

    def is_frozen(self, p):
        elevation = self.map[p[0], p[1]]
        equator = (settings.MAP_HEIGHT // 2) + self.tilt
        steps_from_equator = (abs(equator - p[1]) + 1) * .1
        frosty_range = (elevation * 2 + steps_from_equator) / 3.0
        return frosty_range > self.freezing_zone

