from dataclasses import dataclass

from components.events.die_events import DeathListener
from components.events.tree_cut_event import TreeCutEvent


@dataclass
class TreeCutOnDeath(DeathListener):
    """Signal that a tree has been cut down."""

    def on_die(self, scene):
        self._log_debug(f"triggered")
        scene.cm.add(TreeCutEvent(entity=scene.player))
