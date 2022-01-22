from dataclasses import dataclass

from engine.base_components.energy_actor import EnergyActor
from components.brains.painters.painter_brain import PainterBrain
from content.getables.gold import make_gold_nugget
from engine import constants


@dataclass
class PlaceGoldController(PainterBrain):
    energy_cost: int = EnergyActor.INSTANT
    cursor: int = constants.INVALID

    def paint_one(self, scene, position):
        return make_gold_nugget(position[0], position[1])[1]
