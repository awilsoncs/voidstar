from dataclasses import dataclass

from engine.components.component import Component


@dataclass
class Options(Component):
    show_breadcrumbs: bool = False
