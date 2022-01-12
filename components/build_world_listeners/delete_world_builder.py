import logging
from dataclasses import dataclass

from components.build_world_listeners.build_world_listeners import BuildWorldListener


@dataclass
class DeleteWorldBuilder(BuildWorldListener):
    def on_build_world(self, scene):
        self._log_info(f"cleaning up world builder")
        scene.cm.delete(self.entity)
