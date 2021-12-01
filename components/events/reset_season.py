from dataclasses import dataclass
import random
from typing import List

import settings
from components import Attributes, Coordinates
from components.actors.energy_actor import EnergyActor
from components.tax_value import TaxValue
from content.allies import make_peasant
from content.houses import make_house
from engine.core import log_debug
from engine.utilities import get_3_by_3_square


@dataclass
class ResetSeason(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT

    @log_debug(__name__)
    def act(self, scene):
        reset_healths(scene)
        collect_taxes(scene)
        migrate_villagers(scene)
        scene.cm.delete_component(self)


def reset_healths(scene):
    scene.popup_message("You rest and your wounds heal.")
    healths: List[Attributes] = scene.cm.get(Attributes)
    for health in healths:
        health.hp = health.max_hp


def collect_taxes(scene):
    taxes: List[TaxValue] = scene.cm.get(TaxValue)
    collected_taxes = sum(tax.value for tax in taxes)
    scene.popup_message(f'You collect {collected_taxes} gold from the village.')
    scene.gold += collected_taxes


def migrate_villagers(scene) -> None:
    # find a suitable place
    suitable_location = False
    taken_coords = {c.position for c in scene.cm.get(Coordinates)}

    while not suitable_location:
        x = random.randint(5, settings.MAP_WIDTH - 5)
        y = random.randint(5, settings.MAP_HEIGHT - 5)
        home_footprint = get_3_by_3_square(x, y)
        if home_footprint.isdisjoint(taken_coords):
            migrant = make_house(0, x, y) + [make_peasant(0, x, y)]
            for entity in migrant:
                scene.cm.add(*entity[1])
        suitable_location = True
