import logging
from dataclasses import dataclass

import settings
from components.build_world_listeners.build_world_listeners import BuildWorldListener
from components.build_world_listeners.world_parameters import get_plains_params, get_forest_params, \
    get_mountain_params, get_swamp_params, get_tundra_params
from gui.easy_menu import EasyMenu


@dataclass
class SetWorldParameters(BuildWorldListener):
    def on_build_world(self, scene):
        logging.info(f"EID#{self.entity}::SetWorldBuilderParameters setting worldbuilder params")
        scene.gui.add_element(
            EasyMenu(
                "Which region?",
                {
                    "Plains": self.get_settings(scene, get_plains_params),
                    "Forest": self.get_settings(scene, get_forest_params),
                    "Mountains": self.get_settings(scene, get_mountain_params),
                    "Swamp": self.get_settings(scene, get_swamp_params),
                    "Tundra": self.get_settings(scene, get_tundra_params)
                },
                settings.INVENTORY_WIDTH,
            )
        )

    def create_default_params(self, scene):
        def out_fn():
            logging.debug(f"EID#{self.entity}::SetWorldBuilderParameters creating default worldbuilder params")
        return out_fn

    def get_settings(self, scene, factory):
        def out_fn():
            scene.cm.add(factory(scene.player))
        return out_fn
