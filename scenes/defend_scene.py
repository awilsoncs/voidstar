import numpy as np
import tcod
import tcod.map

import settings
from components import Attributes
from components.coordinates import Coordinates
from components.material import Material
from engine import GameScene, colors, core
from engine.constants import PLAYER_ID
from engine.infos import ColoredMessage
from gui.bars import Bar
from gui.fps_counter import FPSCounter
from gui.message_box import MessageBox
from gui.play_window import PlayWindow
from procgen.town_names import get_file_name
from procgen.zonebuilders import fields
from systems import ai, control_player, death, \
    debug_system, interact, update_senses, \
    move, control_turns, quit, melee_attack, control_cursor, dungeon_master


class DefendScene(GameScene):
    def __init__(self, peasants, monsters, debug=False):
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
        self.add_gui_element(self.play_window)
        self.add_gui_element(FPSCounter(1, 49))
        self.add_gui_element(MessageBox(30, 0, 30, 5, self.message_box))

        self.hp_bar = None
        self.zone_id = core.get_id()
        self.monsters = monsters
        self.peasants = peasants

    def on_load(self):
        self.cm.connect(get_file_name())
        self.setup_level()

    def get_hp_bar(self):
        health = self.cm.get_one(Attributes, self.player)
        return Bar(
            x=1, y=1, total_width=23,
            name='health',
            value=lambda: health.hp,
            maximum=lambda: health.max_hp,
            bar_color=colors.light_red,
            back_color=colors.dark_red
        )

    def update(self):
        try:
            ai.run(self)
            control_player.run(self)
            control_cursor.run(self)
            death.run(self)
            debug_system.run(self)
            interact.run(self)
            melee_attack.run(self)
            move.run(self)
            control_turns.run(self)
            update_senses.run(self)
            dungeon_master.run(self)
            quit.run(self)
        except Exception as e:
            if self.debug:
                raise e
            self.message(str(e), color=colors.red)

    def on_unload(self):
        self.cm.delete(PLAYER_ID)
        self.cm.freeze()

    def message(self, message, color=colors.white):
        self.message_box.append(ColoredMessage(
            color=color,
            message=message
        ))

    def setup_level(self):
        fields.build(self.cm, self.zone_id, peasants=self.peasants, monsters=self.monsters)
        self.cm.thaw(self.zone_id)

        # load up the transparency map
        self.play_window.cm = self.cm
        if not self.hp_bar:
            self.hp_bar = self.get_hp_bar()
            self.add_gui_element(self.hp_bar)

        coordinates = self.cm.get(Coordinates)
        coordinates = [c for c in coordinates if c.terrain]

        for coord in coordinates:
            material = self.cm.get_one(Material, coord.entity)
            self.map.transparent[coord.x, coord.y] = not material.blocks_sight if material else True
            self.map.walkable[coord.x, coord.y] = not material.blocks if material else True

    def next_level(self):
        self.controller.next_level(self.monsters, self.monsters + self.peasants)
