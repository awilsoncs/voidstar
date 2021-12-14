import numpy as np
import tcod
import tcod.map

import settings
from components import clear_components
from components.coordinates import Coordinates
from components.events.chargeabilityevent import ChargeAbilityEvent
from components.material import Material
from content.utilities import make_calendar
from engine import GameScene, core, palettes
from engine.constants import PLAYER_ID
from engine.core import timed
from engine.infos import ColoredMessage
from gui.bars import HealthBar, PeasantBar, HordelingBar, Thwackometer, Shootometer
from gui.help_tab import HelpTab
from gui.labels import Label, GoldLabel, CalendarLabel, HordeStatusLabel, SwampedLabel
from gui.play_window import PlayWindow
from gui.vertical_anchor import VerticalAnchor
from systems import act, death, \
    debug_system, update_senses, pickup_gold, \
    move, control_turns, quit, melee_attack, control_cursor, thwack, peasant_dead_check


class DefendScene(GameScene):
    def __init__(self, zonebuilder=None, debug=True):
        super().__init__(debug)
        self.player = PLAYER_ID
        self.message_box = []
        self.zonebuilder = zonebuilder

        self.map = tcod.map.Map(settings.MAP_WIDTH, settings.MAP_HEIGHT, order='F')
        # track tiles the player has seen
        self.memory_map = np.zeros((settings.MAP_WIDTH, settings.MAP_HEIGHT), order='F', dtype=bool)

        # build out the gui
        self.play_window = PlayWindow(
            25, 0, settings.MAP_WIDTH, settings.MAP_HEIGHT,
            self.cm, self.map.fov, self.memory_map
        )

        anchor = VerticalAnchor(1, 1)
        anchor.add_space(1)

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
        anchor.add_space(14)

        anchor.add_element(HelpTab(1, 30))

        self.add_gui_element(anchor)
        self.add_gui_element(self.play_window)
        # self.add_gui_element(FPSCounter(1, 49))

        self.zone_id = core.get_id()
        self.peasants = 3
        self.gold = 0

    def on_load(self):
        self.cm.clear()
        self.setup_level()

    @timed(100, __name__)
    def update(self):
        try:
            act.run(self)
            death.run(self)
            debug_system.run(self)
            thwack.run(self)
            melee_attack.run(self)
            move.run(self)
            update_senses.run(self)
            pickup_gold.run(self)
            peasant_dead_check.run(self)

            clear_components.of_type(ChargeAbilityEvent, self)
            control_turns.run(self)
            quit.run(self)

        except Exception as e:
            if self.debug:
                raise e
            self.message(str(e), color=palettes.BLOOD)

    def on_unload(self):
        self.cm.delete(PLAYER_ID)
        self.cm.clear()

    def message(self, message, color=palettes.WHITE):
        self.message_box.append(ColoredMessage(
            color=color,
            message=message
        ))

    def setup_level(self):
        self.zonebuilder.build(self.cm)

        # load up the transparency map
        self.play_window.cm = self.cm

        coordinates = self.cm.get(Coordinates)
        coordinates = [c for c in coordinates if c.terrain]

        self.map.transparent.fill(True)

        self.cm.add(*make_calendar()[1])

        for coord in coordinates:
            material = self.cm.get_one(Material, coord.entity)
            self.map.transparent[coord.x, coord.y] = not material.blocks_sight if material else True
            self.map.walkable[coord.x, coord.y] = not material.blocks if material else True

        self.popup_message("You have been tasked with protecting the peasants of the Toshim Plains.")
        self.popup_message("At the end of each season, the horde will come, ravenous in hunger.")
