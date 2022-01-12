import time
from dataclasses import dataclass, field

import settings
from engine.component import Component

DEFAULT_LAKES: int = 1
DEFAULT_LAKE_PROLIFERATION: float = 0.2
DEFAULT_COPSE: int = 10
DEFAULT_COPSE_PROLIFERATION: float = 0.05
DEFAULT_ROCKS: int = 2
DEFAULT_ROCKS_PROLIFERATION: float = 0.075
DEFAULT_FLOWERS: int = 10
DEFAULT_FLOWER_PROLIFERATION: float = 0.1
DEFAULT_TEMPERATURE_MODIFIER: int = 0
DEFAULT_RIVER_RAPIDS: int = 5000
DEFAULT_TREE_CUT_ANGER: int = 1


def get_seed():
    return time.time_ns() if settings.SEED == "RANDOM" else settings.SEED


@dataclass
class WorldParameters(Component):
    biome: str = 'Plains'

    lakes: int = DEFAULT_LAKES
    lake_proliferation: float = DEFAULT_LAKE_PROLIFERATION

    copse: int = DEFAULT_COPSE
    copse_proliferation: float = DEFAULT_COPSE_PROLIFERATION

    rock_fields: int = DEFAULT_ROCKS
    rocks_proliferation: float = DEFAULT_ROCKS_PROLIFERATION

    flower_fields: int = DEFAULT_FLOWERS
    flower_proliferation: float = DEFAULT_FLOWER_PROLIFERATION

    temperature_modifier: int = DEFAULT_TEMPERATURE_MODIFIER

    is_water_swampy: bool = False
    river_rapids: int = DEFAULT_RIVER_RAPIDS

    # how much cutting a tree angers the nature spirit
    tree_cut_anger: int = DEFAULT_TREE_CUT_ANGER

    world_name: str = ''

    world_seed: int = field(default_factory=get_seed)

    def get_file_name(self):
        return self.world_name.replace(" ", "-")


def get_plains_params(entity):
    return WorldParameters(entity=entity)


def get_forest_params(entity):
    return WorldParameters(
        biome='Forest',
        entity=entity,
        copse=DEFAULT_COPSE*20,
        flower_fields=DEFAULT_FLOWERS//2,
        flower_proliferation=DEFAULT_FLOWER_PROLIFERATION/2,
        tree_cut_anger=DEFAULT_TREE_CUT_ANGER*2
    )


def get_mountain_params(entity):
    return WorldParameters(
        entity=entity,
        biome='Mountain',
        copse=DEFAULT_COPSE//2,
        copse_proliferation=DEFAULT_COPSE_PROLIFERATION/2,
        rock_fields=DEFAULT_ROCKS*40,
        rocks_proliferation=DEFAULT_ROCKS_PROLIFERATION*2,
        lakes=0,
        temperature_modifier=DEFAULT_TEMPERATURE_MODIFIER-5,
        river_rapids=DEFAULT_RIVER_RAPIDS//5
    )


def get_swamp_params(entity):
    return WorldParameters(
        entity=entity,
        biome='Swamp',
        copse=DEFAULT_COPSE*10,
        copse_proliferation=DEFAULT_COPSE_PROLIFERATION/2,
        lakes=DEFAULT_LAKES*100,
        lake_proliferation=DEFAULT_LAKE_PROLIFERATION/2,
        rocks_proliferation=0,
        temperature_modifier=DEFAULT_TEMPERATURE_MODIFIER + 5,
        is_water_swampy=True
    )


def get_tundra_params(entity):
    return WorldParameters(
        entity=entity,
        biome='Tundra',
        copse=0,
        rock_fields=DEFAULT_ROCKS*10,
        rocks_proliferation=DEFAULT_ROCKS_PROLIFERATION*2,
        lakes=DEFAULT_LAKES*100,
        lake_proliferation=DEFAULT_LAKE_PROLIFERATION/2,
        temperature_modifier=DEFAULT_TEMPERATURE_MODIFIER-20,
        is_water_swampy=True
    )
