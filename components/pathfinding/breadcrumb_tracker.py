import logging
from dataclasses import dataclass, field
from typing import List, Tuple

from content.breadcrumb import make_breadcrumb
from engine.component import Component


@dataclass
class BreadcrumbTracker(Component):
    breadcrumbs: List[int] = field(default_factory=list)

    def add_breadcrumbs(self, scene, path: List[Tuple[int, int]]):
        logging.debug(f"EID#{self.entity}::BreadcrumbTracker adding breadcrumbs to scene")
        new_breadcrumbs = []
        for path_node in path:
            breadcrumb = make_breadcrumb(path_node[0], path_node[1])
            new_breadcrumbs.append(breadcrumb[0])
            scene.cm.add(*breadcrumb[1])
        for breadcrumb in self.breadcrumbs:
            scene.cm.delete(breadcrumb)
        self.breadcrumbs = new_breadcrumbs

    def on_component_delete(self, cm):
        for breadcrumb in self.breadcrumbs:
            cm.delete(breadcrumb)
