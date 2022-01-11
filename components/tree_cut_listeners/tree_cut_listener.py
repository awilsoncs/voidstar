from abc import ABC, abstractmethod

from engine.component import Component


class TreeCutListener(Component, ABC):

    @abstractmethod
    def on_tree_cut(self, scene):
        raise NotImplementedError()
