import logging
from dataclasses import dataclass

from components.actors.energy_actor import EnergyActor
from engine import palettes
from engine.serialization import serialization


@dataclass
class LoadGame(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT

    def act(self, scene) -> None:
        logging.info(f"EID#{self.entity}::LoadGame attempting to read game")
        scene.cm.delete_component(self)
        data = serialization.load('./game_save.json')
        scene.cm.from_list(data)
        logging.info(f"EID#{self.entity}::LoadGame read complete")
        scene.message("Game loaded.", color=palettes.LIGHT_WATER)



