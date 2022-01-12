from dataclasses import dataclass

from components.actors.energy_actor import EnergyActor
from components.brains.painters.painter_brain import PainterBrain
from content.enemies.juvenile import make_juvenile
from engine import constants


@dataclass
class PlaceHordelingController(PainterBrain):
    energy_cost: int = EnergyActor.INSTANT
    cursor: int = constants.INVALID

    def paint_one(self, scene, position):
        return make_juvenile(position[0], position[1])[1]
