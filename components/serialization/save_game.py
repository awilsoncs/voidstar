import logging
from dataclasses import dataclass

from components.actors.energy_actor import EnergyActor
from engine import palettes
from engine.serialization import serialization


@dataclass
class SaveGame(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT

    def act(self, scene) -> None:
        logging.info(f"EID#{self.entity}::SaveGame attempting to save game")
        # we don't want this object to get caught in the save game
        scene.cm.delete_component(self)
        serialization.save(scene.cm.components_by_id, './game_save.json')
        logging.info(f"EID#{self.entity}::SaveGame save complete")
        scene.message("Game saved.", color=palettes.LIGHT_WATER)

