import logging
from dataclasses import dataclass

from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from components.tree_cut_listeners.tree_cut_listener import TreeCutListener
from engine import palettes


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
            self.spirits_wrath += 1
            self.spirits_attitude = max(1, self.spirits_attitude - 1)

    def on_season_reset(self, scene, season):
        if season == "Spring":
            logging.info(f"EID#{self.entity}::WorldBeauty relationship with the spirits improved")
            self.spirits_attitude += 1
            self.spirits_wrath -= 1
