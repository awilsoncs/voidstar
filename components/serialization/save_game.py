from dataclasses import dataclass, field
from typing import Dict

from engine.base_components.energy_actor import EnergyActor
from components.world_building.world_parameters import WorldParameters
from engine import palettes, core, serialization


@dataclass
class SaveGame(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT
    extra: Dict = field(default_factory=dict)

    def act(self, scene) -> None:
        # we don't want this object to get caught in the save game
        scene.cm.delete_component(self)

        self._log_info(f"attempting to save game")
        params = scene.cm.get_one(WorldParameters, entity=core.get_id("world"))
        serialization.save(scene.cm.get_serial_form(), f"./{params.get_file_name()}.world", self.extra)
        self._log_info(f"save complete")
        scene.message("Game saved.", color=palettes.LIGHT_WATER)

