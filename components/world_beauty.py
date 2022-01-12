import logging
from dataclasses import dataclass

from components.build_world_listeners.world_parameters import WorldParameters
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from components.tree_cut_listeners.tree_cut_listener import TreeCutListener
from engine import palettes, core


@dataclass
class WorldBeauty(TreeCutListener, SeasonResetListener):
    trees_cut: int = 0
    spirits_wrath: int = 0
    spirits_attitude: int = 10

    def on_tree_cut(self, scene):
        logging.info(f"EID#{self.entity}::WorldBeauty detected tree cut")
        self.trees_cut += 1
        if not self.trees_cut % self.spirits_attitude:
            scene.message("The spirits grow angrier with your cutting.", color=palettes.BLOOD)
            world_params = scene.cm.get_one(WorldParameters, entity=core.get_id("world"))
            self.spirits_wrath += 1
            self.spirits_attitude = max(1, self.spirits_attitude - world_params.tree_cut_anger)
            logging.info(f"EID#{self.entity}::WorldBeauty decreased wrath {self.spirits_wrath} and "
                         f"attitude {self.spirits_attitude}")

    def on_season_reset(self, scene, season):
        if season == "Spring":
            logging.info(f"EID#{self.entity}::WorldBeauty relationship with the spirits improved")
            self.spirits_attitude += 1
            self.spirits_wrath -= 1
            logging.info(f"EID#{self.entity}::WorldBeauty improved wrath {self.spirits_wrath} and "
                         f"attitude {self.spirits_attitude}")

