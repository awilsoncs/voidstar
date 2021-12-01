from dataclasses import dataclass

from components import Attributes
from components.abilities.thwack_ability import ThwackAbility
from components.states.dizzy_state import DizzyState
from components.tags.hordeling_tag import HordelingTag
from components.tags.peasant_tag import PeasantTag
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
        peasants = len(scene.cm.get(PeasantTag))
        self.value = peasants
        self.max_value = peasants


@dataclass
class HordelingBar(Bar):
    symbol: str = 'h'
    fg_color: tuple = palettes.HORDELING
    mg_color: tuple = palettes.BLOOD

    def update(self, scene):
        hordelings = len(scene.cm.get(HordelingTag))
        self.value = hordelings
        self.max_value = hordelings


@dataclass
class Thwackometer(Bar):
    symbol: str = '/'

    fg_color: tuple = palettes.STONE
    mg_color: tuple = palettes.GABRIEL_3_5

    thwack_fg: tuple = palettes.STONE
    thwack_mg: tuple = palettes.GABRIEL_3_5

    dizzy_fg: tuple = palettes.LIGHT_WATER
    dizzy_mg: tuple = palettes.GABRIEL_2_2

    max: int = 0  # we'll need this when the player dies

    def update(self, scene):
        thwack_ability = scene.cm.get_one(ThwackAbility, entity=PLAYER_ID)
        dizzy = scene.cm.get_one(DizzyState, entity=PLAYER_ID)

        if not dizzy:
            self.symbol = '/'
            self.fg_color = self.thwack_fg
            self.mg_color = self.thwack_mg

            self.value = thwack_ability.count if thwack_ability else 0
            self.max = thwack_ability.max if thwack_ability else self.max
            self.max_value = thwack_ability.max if thwack_ability else self.max
        else:
            self.symbol = '?'
            self.fg_color = self.dizzy_fg
            self.mg_color = self.dizzy_mg

            self.value = dizzy.duration
            self.max_value = 3

