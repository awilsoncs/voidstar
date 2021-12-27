from dataclasses import dataclass

from engine.component import Component


@dataclass
class Residence(Component):
    house_id: int = 0