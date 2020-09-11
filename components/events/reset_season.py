from dataclasses import dataclass
from typing import List

from components import TimedActor, Attributes
from components.tax_value import TaxValue
from engine import core
from engine.core import log_debug


@dataclass
class ResetSeason(TimedActor):
    timer_delay: int = TimedActor.REAL_TIME

    @log_debug(__name__)
    def act(self, scene):
        reset_healths(scene)
        collect_taxes(scene)
        scene.cm.delete_component(self)


def reset_healths(scene):
    healths: List[Attributes] = scene.cm.get(Attributes)
    for health in healths:
        health.hp = health.max_hp


def collect_taxes(scene):
    taxes: List[TaxValue] = scene.cm.get(TaxValue)
    for tax in taxes:
        scene.gold += tax.value
