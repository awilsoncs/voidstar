from dataclasses import dataclass

from engine.component import Component


@dataclass
class Options(Component):
    show_breadcrumbs: bool = False
