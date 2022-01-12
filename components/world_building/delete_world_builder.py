from dataclasses import dataclass

from components.events.build_world_events import BuildWorldListener


@dataclass
class DeleteWorldBuilder(BuildWorldListener):
    def on_build_world(self, scene):
        self._log_info(f"cleaning up world builder")
        scene.cm.delete(self.entity)
