from dataclasses import dataclass
import random

from components.build_world_listeners.build_world_listeners import BuildWorldListener
from components.build_world_listeners.world_parameters import WorldParameters
from engine import core
from procgen import town_names


@dataclass
class SetWorldName(BuildWorldListener):
    def on_build_world(self, scene):
        world_params = scene.cm.get_one(WorldParameters, entity=core.get_id("world"))
        if random.random() > 0.5:
            world_params.world_name = f"{town_names.get_name()} {world_params.biome}"
        else:
            world_params.world_name = f"{world_params.biome} of {town_names.get_name()}"
