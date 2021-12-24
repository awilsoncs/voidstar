import logging
from dataclasses import dataclass

import settings
from components.build_world_listeners.build_world_listeners import BuildWorldListener
from content.player import make_player


@dataclass
class AddPlayerStep(BuildWorldListener):
    def on_build_world(self, scene):
        logging.info(f"EID#{self.entity}::AddPlayerStep adding player to map")
        player = make_player(settings.MAP_HEIGHT // 2, settings.MAP_WIDTH // 2)
        scene.cm.add(*player[1])
