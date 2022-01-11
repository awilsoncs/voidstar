import logging
from dataclasses import dataclass

from components.death_listeners.death_listener import DeathListener
from components.tree_cut_listeners.tree_cut_event import TreeCutEvent


@dataclass
class TreeCutOnDeath(DeathListener):
    """Signal that a tree has been cut down."""

    def on_die(self, scene):
        logging.info(f"EID#{self.entity}::TreeCutOnDeath triggered")
        scene.cm.add(TreeCutEvent(entity=scene.player))
