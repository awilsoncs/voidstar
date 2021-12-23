import numpy as np

import settings
from components import clear_components
from components.events.chargeabilityevent import ChargeAbilityEvent
from components.game_start_listeners.start_game import StartGame
from content.physics_controller import make_physics_controller
from content.utilities import make_calendar
from content.world_builder import make_world_build
from engine import GameScene
from engine.component_manager import ComponentManager
from engine.constants import PLAYER_ID
from engine.core import timed
from gui.bars import HealthBar, PeasantBar, HordelingBar, Thwackometer, Shootometer
from gui.help_tab import HelpTab
from gui.labels import Label, GoldLabel, CalendarLabel, HordeStatusLabel, SwampedLabel
from gui.play_window import PlayWindow
from gui.vertical_anchor import VerticalAnchor
from systems import act, death, \
    pickup_gold, \
    move, control_turns, quit, melee_attack, thwack, peasant_dead_check


class DefendScene(GameScene):
    def __init__(self, debug=True):
        super().__init__(debug)
        self.player = PLAYER_ID

        # track tiles the player has seen
        self.memory_map = np.zeros((settings.MAP_WIDTH, settings.MAP_HEIGHT), order='F', dtype=bool)
        self.visibility_map = np.zeros((settings.MAP_WIDTH, settings.MAP_HEIGHT), order='F', dtype=bool)

        # build out the gui
        self.play_window = PlayWindow(
            25, 0, settings.MAP_WIDTH, settings.MAP_HEIGHT,
            self.cm, self.visibility_map
            , self.memory_map
        )

        anchor = VerticalAnchor(1, 1)
        # anchor.add_space(1)

        anchor.add_element(Label(1, 1, settings.CHARACTER_NAME))
        anchor.add_element(HealthBar(1, 2))
        anchor.add_element(Thwackometer(1, 3))
        anchor.add_element(Shootometer(1, 4))
        anchor.add_element(SwampedLabel(1, 5))
        anchor.add_element(CalendarLabel(1, 0))
        anchor.add_element(GoldLabel(1, 0))
        anchor.add_space(1)

        anchor.add_element(Label(1, 5, "Peasants"))
        anchor.add_element(PeasantBar(1, 6))
        anchor.add_space(1)

        anchor.add_element(HordeStatusLabel(1, 8))
        anchor.add_element(HordelingBar(1, 9))
        anchor.add_space(12)

        anchor.add_element(HelpTab(1, 26))

        self.add_gui_element(anchor)
        self.add_gui_element(self.play_window)

        self.gold = 0

    def on_load(self):
        self.cm = ComponentManager()
        self.play_window.cm = self.cm
        self.cm.add(*make_world_build()[1])
        self.cm.add(*make_calendar()[1])
        self.cm.add(*make_physics_controller()[1])
        self.cm.add(StartGame(entity=self.player))

    @timed(100, __name__)
    def update(self):
        act.run(self)
        death.run(self)
        thwack.run(self)
        move.run(self)
        pickup_gold.run(self)
        peasant_dead_check.run(self)
        clear_components.of_type(ChargeAbilityEvent, self)
        control_turns.run(self)
        quit.run(self)
