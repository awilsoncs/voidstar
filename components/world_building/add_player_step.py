from dataclasses import dataclass

import settings
from components.events.build_world_events import BuildWorldListener
from content.player import make_player


@dataclass
class AddPlayerStep(BuildWorldListener):
    def on_build_world(self, scene):
        self._log_info(f"adding player to map")
        player = make_player(settings.MAP_FRAME_HEIGHT // 2, settings.MAP_FRAME_WIDTH // 2)
        scene.cm.add(*player[1])
