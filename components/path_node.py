from dataclasses import dataclass

from components.component import Component


@dataclass
class PathNode(Component):
    step: int = 0
    x: int = 0
    y: int = 0


def create_path(entity, path):
    return [
        PathNode(entity=entity, step=step, x=location[0], y=location[1])
        for step, location in enumerate(path)
    ]
