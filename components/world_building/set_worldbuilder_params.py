import random
from dataclasses import dataclass

import settings
from components.world_building.world_parameters import get_plains_params, get_forest_params, get_mountain_params, \
    get_swamp_params, get_tundra_params
from content.world_builder import make_world_build
from engine import core
from engine.components.energy_actor import EnergyActor
from gui.easy_menu import EasyMenu


def get_settings(scene, factory):
    def out_fn():
        params = factory(core.get_id("world"))
        random.seed(params.world_seed)
        scene.cm.add(params, *make_world_build()[1])
    return out_fn


@dataclass
class SelectBiome(EnergyActor):
    def act(self, scene):
        self._log_info(f"setting worldbuilder params")
        scene.gui.add_element(
            EasyMenu(
                "Which region?",
                {
                    "Plains (Easy)": get_settings(scene, get_plains_params),
                    "Forest (Moderate)": get_settings(scene, get_forest_params),
                    "Mountains (Hard)": get_settings(scene, get_mountain_params),
                    "Swamp (Hard)": get_settings(scene, get_swamp_params),
                    "Tundra (Brutal)": get_settings(scene, get_tundra_params)
                },
                settings.INVENTORY_WIDTH,
                on_escape=lambda: scene.pop()
            )
        )
        scene.cm.delete_component(self)
