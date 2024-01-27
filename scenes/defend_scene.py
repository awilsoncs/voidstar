from typing import Tuple

import numpy as np

import settings
from engine.components.class_register import LoadClasses
from components.world_building.set_worldbuilder_params import SelectBiome
from components.events.start_game_events import StartGame
from components.serialization.load_game import LoadGame
from components.sound.battle_music import BattleMusic
from components.sound.start_music import StartMusic
from content.physics_controller import make_physics_controller
from engine import GameScene, palettes, core
from engine.component_manager import ComponentManager
from engine.constants import PLAYER_ID
from engine.core import timed
from engine.message import Message
from gui.bars import HealthBar, HordelingBar, Thwackometer
from gui.help_tab import HelpTab
from gui.labels import Label, GoldLabel, SpeedLabel, AbilityLabel, VillageNameLabel
from gui.message_box import MessageBox
from gui.play_window import PlayWindow
from gui.popup_message import PopupMessage
from gui.vertical_anchor import VerticalAnchor
from systems import act, move, control_turns


class DefendScene(GameScene):
    def __init__(self, from_file=''):
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
        anchor.add_element(GoldLabel(1, 0))
        anchor.add_element(AbilityLabel(1, 0))
        anchor.add_space(1)

        anchor.add_element(VillageNameLabel(1, 6))
        anchor.add_element(MessageBox(1, 11, 23, 16, self.messages))
        anchor.add_space(16)

        self.add_gui_element(anchor)
        self.add_gui_element(self.play_window)

        self.gold = 0

        self.from_file = from_file

    def on_load(self):
        self.cm = ComponentManager()
        self.play_window.cm = self.cm
        self.cm.add(LoadClasses(entity=self.player))

        if self.from_file:
            self.cm.add(LoadGame(entity=self.player, file_name=self.from_file))
            self.cm.add(StartGame(entity=self.player))
        else:
            self.cm.add(SelectBiome(entity=core.get_id("world")))
            self.cm.add(*make_physics_controller()[1])
            self.cm.add(StartMusic(entity=self.player))
            self.cm.add(BattleMusic(entity=self.player))

    def popup_message(self, message: str):
        self.message(message)
        self.add_gui_element(PopupMessage(message))

    @timed(100, __name__)
    def update(self):
        act.run(self)
        move.run(self)
        control_turns.run(self)

    def message(self, text: str, color: Tuple[int, int, int] = palettes.MEAT):
        if len(self.messages) > 20:
            self.messages.pop(0)
        self.messages.append(Message(f" {text}", color=color))

    def warn(self, text: str):
        self.message(text, color=palettes.HORDELING)
