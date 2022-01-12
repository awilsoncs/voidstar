from dataclasses import dataclass

from components.events.build_world_events import BuildWorldListener
from content.farmsteads.houses import place_farmstead


@dataclass
class PlacePeasants(BuildWorldListener):
    def on_build_world(self, scene):
        self._log_info(f"placing farmsteads in town")
        for _ in range(3):
            place_farmstead(scene)
