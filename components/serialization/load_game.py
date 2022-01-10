import logging
import os
from dataclasses import dataclass

import settings
from components.actors.energy_actor import EnergyActor
from engine import palettes, core
from engine.serialization import serialization
from gui.easy_menu import EasyMenu


@dataclass
class LoadGame(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT

    def act(self, scene) -> None:
        scene.cm.delete_component(self)

        files = []

        for file in os.listdir("."):
            if file.endswith(".world"):
                files.append(file)

        scene.gui.add_element(
            EasyMenu(
                "Load which?",
                {
                    world: self.get_world_loader(scene, world) for world in files
                },
                settings.INVENTORY_WIDTH,
            )
        )

    def get_world_loader(self, scene, file_name):
        def out_fn():
            self.load_world(scene, file_name)
        return out_fn

    def load_world(self, scene, file_name):
        start = core.time_ms()
        logging.info(f"EID#{self.entity}::LoadGame attempting to read game")
        data = serialization.load(file_name)
        scene.cm.from_list(data)
        end = core.time_ms()
        logging.info(f"EID#{self.entity}::LoadGame loaded {len(data)} objects in {end - start}ms")
        scene.message("Game loaded.", color=palettes.LIGHT_WATER)



