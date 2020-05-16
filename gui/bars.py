from dataclasses import dataclass

from components import Attributes, target_value
from components.tags import Tag
from components.target_value import TargetValue
from engine import palettes, PLAYER_ID
from gui.gui_element import GuiElement


@dataclass
class Bar(GuiElement):
    value: int = 0
    max_value: int = 0
    fg_color: tuple = palettes.WHITE
    mg_color: tuple = palettes.GABRIEL_2_1
    bg_color: tuple = palettes.BACKGROUND
    symbol: str = '!'

    def render(self, panel):
        self._draw(panel, self.mg_color, self.max_value)
        self._draw(panel, self.fg_color, self.value)

    def _draw(self, panel, color, value):
        panel.draw_rect(
            x=self.x,
            y=self.y,
            width=value,
            height=1,
            ch=ord(self.symbol),
            fg=color,
            bg=self.bg_color
        )


@dataclass
class HealthBar(Bar):
    symbol: str = '♥'
    fg_color: tuple = palettes.HORDELING
    mg_color: tuple = palettes.BLOOD

    def update(self, scene):
        player_health = scene.cm.get_one(Attributes, entity=PLAYER_ID)
        if player_health:
            self.value = player_health.hp
            self.max_value = player_health.max_hp
        else:
            self.value = 0


@dataclass
class PeasantBar(Bar):
    symbol: str = 'p'
    fg_color: tuple = palettes.WHITE
    mg_color: tuple = palettes.GABRIEL_2_1

    def update(self, scene):
        peasants = scene.cm.get(Tag)
        peasants = len([p for p in peasants if p.value == 'peasant'])
        self.value = peasants
        self.max_value = scene.peasants


@dataclass
class HordelingBar(Bar):
    symbol: str = 'h'
    fg_color: tuple = palettes.HORDELING
    mg_color: tuple = palettes.BLOOD

    def update(self, scene):
        hordelings = scene.cm.get(Tag)
        hordelings = len([p for p in hordelings if p.value == 'hordeling'])
        self.value = hordelings
        self.max_value = scene.hordelings
