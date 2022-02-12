from dataclasses import dataclass
from typing import List

from components.season_reset_listeners.collect_taxes_for_king import CollectTaxesForKing
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from components.tax_value import TaxValue
from engine import palettes, core


@dataclass
class CollectTaxes(SeasonResetListener):
    def on_season_reset(self, scene, season):
        taxes: List[TaxValue] = scene.cm.get(TaxValue)
        collected_taxes = sum(tax.value for tax in taxes)
        scene.message(f'You collect {collected_taxes}c from the village.', color=palettes.GOLD)
        scene.gold += collected_taxes

        king_taxes = scene.cm.get(CollectTaxesForKing)
        if king_taxes:
            scene.warn(f'The king will collect {king_taxes[0].value}c from you at the end of the year.')
