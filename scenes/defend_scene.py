import numpy as np
import tcod
import tcod.map

import settings
from components.events.chargeabilityevent import ChargeAbilityEvent
from components.coordinates import Coordinates
from components.events.popup_message import PopupMessage
from components.material import Material
from content.utilities import make_calendar
from engine import GameScene, colors, core, palettes
from engine.constants import PLAYER_ID
from engine.core import timed
from engine.infos import ColoredMessage
from gui.bars import HealthBar, PeasantBar, HordelingBar, Thwackometer
from gui.fps_counter import FPSCounter
from gui.help_tab import HelpTab
from gui.labels import Label, GoldLabel, CalendarLabel, HordeStatusLabel, SwampedLabel
from gui.play_window import PlayWindow
from gui.vertical_anchor import VerticalAnchor
from procgen.zonebuilders import fields
from systems import act, death, \
    debug_system, update_senses, pickup_gold, \
    move, control_turns, quit, melee_attack, control_cursor, dungeon_master, thwack
from components import clear_components
from systems.animators import animation_controller


class DefendScene(GameScene):
    def __init__(self, peasants, hordelings, gold=0, debug=True):
        super().__init__(debug)
        self.player = PLAYER_ID
        self.message_box = []
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
        anchor.add_element(SwampedLabel(1, 4))
        anchor.add_element(CalendarLabel(1, 0))
        anchor.add_element(GoldLabel(1, 0))
        anchor.add_space(1)

        anchor.add_element(Label(1, 5, "Peasants"))
        anchor.add_element(PeasantBar(1, 6))
        anchor.add_space(1)

        anchor.add_element(HordeStatusLabel(1, 8))
        anchor.add_element(HordelingBar(1, 9))
        anchor.add_space(20)

        anchor.add_element(HelpTab(1, 30))

        self.add_gui_element(anchor)
        self.add_gui_element(self.play_window)
        #self.add_gui_element(FPSCounter(1, 49))

        self.zone_id = core.get_id()
        self.hordelings = hordelings
        self.peasants = peasants
        self.gold = gold

    def on_load(self):
        self.cm.clear()
        self.setup_level()

    @timed(100, __name__)
    def update(self):
        try:
            act.run(self)

            animation_controller.run(self)

            control_cursor.run(self)
            death.run(self)
            debug_system.run(self)
            thwack.run(self)
            melee_attack.run(self)
            move.run(self)
            control_turns.run(self)
            update_senses.run(self)
            pickup_gold.run(self)
            # dungeon_master.run(self)

            clear_components.of_type(ChargeAbilityEvent, self)
            quit.run(self)

        except Exception as e:
            if self.debug:
                raise e
            self.message(str(e), color=colors.red)

    def on_unload(self):
        self.cm.delete(PLAYER_ID)
        self.cm.clear()

    def message(self, message, color=colors.white):
        self.message_box.append(ColoredMessage(
            color=color,
            message=message
        ))

    def setup_level(self):
        fields.build(
            self.cm,
            self.zone_id,
            peasants=self.peasants,
            monsters=self.hordelings
        )

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


    def next_level(self):
        self.controller.push_scene(
            DefendScene(
                self.peasants + 1,
                self.hordelings + 2,
                self.gold + 5
            )
        )
