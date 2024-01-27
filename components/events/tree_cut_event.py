from abc import ABC, abstractmethod
from dataclasses import dataclass

from engine.components.component import Component
from engine.components.events import Event


@dataclass
class TreeCutEvent(Event):
    def listener_type(self):
        return TreeCutListener

    def notify(self, scene, listener):
        listener.on_tree_cut(scene)


class TreeCutListener(Component, ABC):

    @abstractmethod
    def on_tree_cut(self, scene):
        raise NotImplementedError()
