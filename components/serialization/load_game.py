import logging
from dataclasses import dataclass

from components.actors.energy_actor import EnergyActor
from engine import palettes, core
from engine.serialization import serialization


@dataclass
class LoadGame(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT

    def act(self, scene) -> None:
        scene.cm.delete_component(self)

        start = core.time_ms()
        logging.info(f"EID#{self.entity}::LoadGame attempting to read game")
        data = serialization.load('./game_save.json')
        scene.cm.from_list(data)
        end = core.time_ms()
        logging.info(f"EID#{self.entity}::LoadGame loaded {len(data)} objects in {end - start}ms")
        scene.message("Game loaded.", color=palettes.LIGHT_WATER)



