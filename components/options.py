from dataclasses import dataclass

from engine.base_components.component import Component


@dataclass
class Options(Component):
    show_breadcrumbs: bool = False
