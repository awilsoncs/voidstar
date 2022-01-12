from dataclasses import dataclass

from components.events.events import Event
from components.tree_cut_listeners.tree_cut_listener import TreeCutListener


@dataclass
class TreeCutEvent(Event):
    def listener_type(self):
        return TreeCutListener

    def notify(self, scene, listener):
        listener.on_tree_cut(scene)
