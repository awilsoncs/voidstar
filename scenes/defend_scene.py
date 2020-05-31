import numpy as np
import tcod
import tcod.map

import settings
from components.events.chargeabilityevent import ChargeAbilityEvent
from components.coordinates import Coordinates
from components.material import Material
from engine import GameScene, colors, core, palettes
from engine.constants import PLAYER_ID
from engine.core import timed
from engine.infos import ColoredMessage
from gui.bars import HealthBar, PeasantBar, HordelingBar, Thwackometer
from gui.fps_counter import FPSCounter
from gui.labels import Label
from gui.message_box import MessageBox
from gui.play_window import PlayWindow
from procgen.zonebuilders import fields
from systems import ai, control_player, death, \
    debug_system, update_senses, \
    move, control_turns, quit, melee_attack, control_cursor, dungeon_master, dally, thwack, clear_components
from systems.animators import animate_on_path, animate_float, animation_controller


class DefendScene(GameScene):
    def __init__(self, peasants, hordelings, debug=True):
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

        self.add_gui_element(Label(1, 1, "Chauncey"))
        self.add_gui_element(HealthBar(1, 2))
        self.add_gui_element(Thwackometer(1, 3))

        self.add_gui_element(Label(1, 5, "Peasants"))
        self.add_gui_element(PeasantBar(1, 6))

        self.add_gui_element(Label(1, 8, "Hordelings", fg=palettes.HORDELING))
        self.add_gui_element(HordelingBar(1, 9))

        self.add_gui_element(self.play_window)
        self.add_gui_element(FPSCounter(1, 49))
        self.add_gui_element(MessageBox(30, 0, 30, 5, self.message_box))

        self.zone_id = core.get_id()
        self.hordelings = hordelings
        self.peasants = peasants

    def on_load(self):
        self.cm.clear()
        self.setup_level()

    @timed(100)
    def update(self):
        try:
            ai.run(self)

            animation_controller.run(self)

            control_player.run(self)
            control_cursor.run(self)
            death.run(self)
            debug_system.run(self)
            thwack.run(self)
            melee_attack.run(self)
            move.run(self)
            control_turns.run(self)
            update_senses.run(self)
            dungeon_master.run(self)
            dally.run(self)

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
        fields.build(self.cm, self.zone_id, peasants=self.peasants, monsters=self.hordelings)

        # load up the transparency map
        self.play_window.cm = self.cm

        coordinates = self.cm.get(Coordinates)
        coordinates = [c for c in coordinates if c.terrain]

        self.map.transparent.fill(True)

        for coord in coordinates:
            material = self.cm.get_one(Material, coord.entity)
            self.map.transparent[coord.x, coord.y] = not material.blocks_sight if material else True
            self.map.walkable[coord.x, coord.y] = not material.blocks if material else True

    def next_level(self):
        self.controller.next_level(
            self.peasants + 1,
            self.hordelings + 2
        )
