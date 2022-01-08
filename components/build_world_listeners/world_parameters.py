from dataclasses import dataclass

from engine.component import Component

DEFAULT_LAKES: int = 1
DEFAULT_LAKE_PROLIFERATION: float = 0.2
DEFAULT_COPSE: int = 10
DEFAULT_COPSE_PROLIFERATION: float = 0.05
DEFAULT_ROCKS: int = 2
DEFAULT_ROCKS_PROLIFERATION: float = 0.075


@dataclass
class WorldParameters(Component):
    lakes: int = DEFAULT_LAKES
    lake_proliferation: float = DEFAULT_LAKE_PROLIFERATION

    copse: int = DEFAULT_COPSE
    copse_proliferation: float = DEFAULT_COPSE_PROLIFERATION

    rock_fields: int = DEFAULT_ROCKS
    rocks_proliferation: float = DEFAULT_ROCKS_PROLIFERATION

    temperature_modifier: int = 0


def get_plains_params(entity):
    return WorldParameters(entity=entity)


def get_forest_params(entity):
    return WorldParameters(
        entity=entity,
        copse=DEFAULT_COPSE*20
    )


def get_mountain_params(entity):
    return WorldParameters(
        entity=entity,
        copse=DEFAULT_COPSE//2,
        copse_proliferation=DEFAULT_COPSE_PROLIFERATION/2,
        rock_fields=DEFAULT_ROCKS*40,
        rocks_proliferation=DEFAULT_ROCKS_PROLIFERATION*2,
        lakes=0
    )


def get_swamp_params(entity):
    return WorldParameters(
        entity=entity,
        copse=DEFAULT_COPSE*10,
        copse_proliferation=DEFAULT_COPSE_PROLIFERATION/2,
        lakes=DEFAULT_LAKES*100,
        lake_proliferation=DEFAULT_LAKE_PROLIFERATION/2,
        rocks_proliferation=0
    )
