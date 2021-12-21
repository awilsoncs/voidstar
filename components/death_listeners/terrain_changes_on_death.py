import logging
from dataclasses import dataclass

from components.death_listeners.death_listener import DeathListener
from components.terrain_changed_listeners.terrain_changed_event import TerrainChangedEvent


@dataclass
class TerrainChangedOnDeath(DeathListener):
    """This entity is a part of the terrain and should notify anything that cares about terrain when it dies."""

    def on_die(self, scene):
        logging.info(f"{self.entity}::TerrainChangedOnDeath triggered")
        scene.cm.add(TerrainChangedEvent(entity=scene.player))
