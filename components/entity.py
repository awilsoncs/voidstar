from dataclasses import dataclass

from engine.component import Component


@dataclass
class Entity(Component):
    name: str = ''
    zone: int = None
    abstract: bool = False
    static: bool = False  # if true, hide from 'interact' functionality

    def get_readable_key(self):
        return f'{self.name}@{self.id}'
