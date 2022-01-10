import logging
from dataclasses import dataclass

import settings
from components.actors.energy_actor import EnergyActor
from components.build_world_listeners.world_parameters import WorldParameters
from engine import palettes
from engine.serialization import serialization


@dataclass
class SaveGame(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT

    def act(self, scene) -> None:
        scene.cm.delete_component(self)
        if not settings.AUTOSAVE:
            logging.info(f"EID#{self.entity}::SaveGame autosave is disabled")
            return

        logging.info(f"EID#{self.entity}::SaveGame attempting to save game")
        # we don't want this object to get caught in the save game

        params = scene.cm.get_one(WorldParameters, entity=scene.player)
        serialization.save(scene.cm.components_by_id, f"./{params.get_file_name()}.world")
        logging.info(f"EID#{self.entity}::SaveGame save complete")
        scene.message("Game saved.", color=palettes.LIGHT_WATER)

