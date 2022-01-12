import logging
from dataclasses import dataclass

import settings
from components.build_world_listeners.build_world_listeners import BuildWorldListener
from content.terrain.trees import make_wall_tree


def add_wall_tree(scene, x: int, y: int) -> None:
    tree = make_wall_tree(x, y)
    scene.cm.add(*tree[1])


@dataclass
class PlaceMapBoundary(BuildWorldListener):
    def on_build_world(self, scene):
        self._log_info(f"placing hardy trees in town")
        for x in range(0, settings.MAP_WIDTH):
            add_wall_tree(scene, x, 0)
            add_wall_tree(scene, x, settings.MAP_HEIGHT - 1)

        for y in range(1, settings.MAP_HEIGHT - 1):
            add_wall_tree(scene, 0, y)
            add_wall_tree(scene, settings.MAP_WIDTH - 1, y)
