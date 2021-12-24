import logging
from dataclasses import dataclass

from components.build_world_listeners.build_world_listeners import BuildWorldListener
from content.farmsteads.houses import place_farmstead


@dataclass
class PlacePeasants(BuildWorldListener):
    def on_build_world(self, scene):
        logging.info(f"EID#{self.entity}::PlacePeasants placing farmsteads in town")
        for _ in range(3):
            place_farmstead(scene)
