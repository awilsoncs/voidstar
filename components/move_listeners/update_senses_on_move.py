import numpy as np
import tcod

import settings
from components import Coordinates
from components.game_start_listeners.game_start_listener import GameStartListener
from components.material import Material
from components.move_listeners.move_listener import MoveListener


class UpdateSensesOnMove(MoveListener, GameStartListener):
    def on_game_start(self, scene):
        self.refresh_fov(scene)

    def on_move(self, scene):
        self.refresh_fov(scene)

    def refresh_fov(self, scene):
        mob = scene.cm.get_one(Coordinates, entity=self.entity)
        transparency = np.ones((settings.MAP_WIDTH, settings.MAP_HEIGHT), order='F', dtype=bool)
        materials = scene.cm.get(Material, query=lambda m: m.blocks_sight)
        for material in materials:
            coords = scene.cm.get_one(Coordinates, entity=material.entity)
            transparency[coords.x, coords.y] = False
            scene.visibility_map[:] = tcod.map.compute_fov(transparency, (mob.x, mob.y))
