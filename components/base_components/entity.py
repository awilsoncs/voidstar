from dataclasses import dataclass

from components.base_components.component import Component


@dataclass
class Entity(Component):
    name: str = ''
    abstract: bool = False
    static: bool = False  # if true, hide from 'interact' functionality
    description: str = ''

    def get_readable_key(self):
        return f'{self.name}@{self.id}'
