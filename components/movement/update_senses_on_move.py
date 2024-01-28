import numpy as np
import tcod

import settings
from components import Coordinates
from components.events.attack_started_events import AttackStartListener
from components.events.start_game_events import GameStartListener
from components.material import Material
from components.events.step_event import StepListener
from components.events.terrain_changed_event import TerrainChangedListener


class UpdateSenses(StepListener, GameStartListener, TerrainChangedListener, AttackStartListener):
    def on_attack_start(self, scene):
        self.refresh_fov(scene)

    def on_game_start(self, scene):
        self.refresh_fov(scene)

    def on_step(self, scene, point):
        self.refresh_fov(scene)

    def on_terrain_changed(self, scene):
        self.refresh_fov(scene)

    def refresh_fov(self, scene):
        mob = scene.cm.get_one(Coordinates, entity=self.entity)
        transparency = np.ones((settings.MAP_FRAME_WIDTH, settings.MAP_FRAME_HEIGHT), order='F', dtype=bool)
        materials = scene.cm.get(Material, query=lambda m: m.blocks_sight)
        for material in materials:
            coords = scene.cm.get_one(Coordinates, entity=material.entity)
            transparency[coords.x, coords.y] = False
            scene.visibility_map[:] = tcod.map.compute_fov(
                transparency,
                (mob.x, mob.y),
                light_walls=True,
                radius=settings.TORCH_RADIUS
            )
