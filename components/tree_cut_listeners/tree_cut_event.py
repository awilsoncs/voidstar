from dataclasses import dataclass
from typing import List

from components.actors.energy_actor import EnergyActor
from components.tree_cut_listeners.tree_cut_listener import TreeCutListener
from engine.core import log_debug


@dataclass
class TreeCutEvent(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT

    @log_debug(__name__)
    def act(self, scene):
        actors: List[TreeCutListener] = scene.cm.get(TreeCutListener)
        for actor in actors:
            actor.on_tree_cut(scene)

        scene.cm.delete_component(self)
