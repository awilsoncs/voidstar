from typing import Tuple

import numpy as np

import settings
from components import clear_components
from components.events.chargeabilityevent import ChargeAbilityEvent
from components.game_start_listeners.start_game import StartGame
from components.sound_events.battle_music import BattleMusic
from components.sound_events.start_music import StartMusic
from content.physics_controller import make_physics_controller
from content.utilities import make_calendar
from content.world_builder import make_world_build
from engine import GameScene, palettes
from engine.component_manager import ComponentManager
from engine.constants import PLAYER_ID
from engine.core import timed
from engine.message import Message
from gui.bars import HealthBar, PeasantBar, HordelingBar, Thwackometer
from gui.help_tab import HelpTab
from gui.labels import Label, GoldLabel, CalendarLabel, HordeStatusLabel, SpeedLabel, AbilityLabel
from gui.message_box import MessageBox
from gui.play_window import PlayWindow
from gui.vertical_anchor import VerticalAnchor
from systems import act, death, \
    pickup_gold, \
    move, control_turns, quit, peasant_dead_check


class DefendScene(GameScene):
    def __init__(self):
        super().__init__()
        self.player = PLAYER_ID

        # track tiles the player has seen
        self.memory_map = np.zeros((settings.MAP_WIDTH, settings.MAP_HEIGHT), order='F', dtype=bool)
        self.visibility_map = np.zeros((settings.MAP_WIDTH, settings.MAP_HEIGHT), order='F', dtype=bool)
        self.messages = []

        # build out the gui
        self.play_window = PlayWindow(
            25, 0, settings.MAP_WIDTH, settings.MAP_HEIGHT,
            self.cm, self.visibility_map
            , self.memory_map
        )

        anchor = VerticalAnchor(1, 1)
        anchor.add_element(Label(1, 1, f'@ {settings.CHARACTER_NAME}_______________'))
        anchor.add_element(HealthBar(1, 0))
        anchor.add_element(Thwackometer(1, 0))
        anchor.add_element(SpeedLabel(1, 0))
        anchor.add_element(CalendarLabel(1, 0))
        anchor.add_element(GoldLabel(1, 0))
        anchor.add_element(AbilityLabel(1, 0))
        anchor.add_space(1)

        anchor.add_element(Label(1, 6, "Village___________________"))
        anchor.add_element(Label(1, 7, "Peasants"))
        anchor.add_element(PeasantBar(1, 8))
        anchor.add_element(HordeStatusLabel(1, 9))
        anchor.add_element(HordelingBar(1, 10))
        anchor.add_element(MessageBox(1, 11, 23, 16, self.messages))
        anchor.add_space(16)

        anchor.add_element(HelpTab(1, 27))

        self.add_gui_element(anchor)
        self.add_gui_element(self.play_window)

        self.gold = 0

    def on_load(self):
        self.cm = ComponentManager()
        self.play_window.cm = self.cm
        self.cm.add(*make_world_build()[1])
        self.cm.add(*make_calendar()[1])
        self.cm.add(*make_physics_controller()[1])
        self.cm.add(StartMusic(entity=self.player))
        self.cm.add(BattleMusic(entity=self.player))
        self.cm.add(StartGame(entity=self.player))

    @timed(100, __name__)
    def update(self):
        act.run(self)
        death.run(self)
        move.run(self)
        pickup_gold.run(self)
        peasant_dead_check.run(self)
        clear_components.of_type(ChargeAbilityEvent, self)
        control_turns.run(self)
        quit.run(self)

    def message(self, text: str, color: Tuple[int, int, int] = palettes.MEAT):
        if len(self.messages) > 20:
            self.messages.pop(0)
        self.messages.append(Message(f" {text}", color=color))

    def warn(self, text: str):
        self.message(text, color=palettes.HORDELING)
