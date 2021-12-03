from dataclasses import dataclass
from typing import List

from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from components.tax_value import TaxValue


@dataclass
class CollectTaxes(SeasonResetListener):
    def on_season_reset(self, scene):
        taxes: List[TaxValue] = scene.cm.get(TaxValue)
        collected_taxes = sum(tax.value for tax in taxes)
        scene.popup_message(f'You collect {collected_taxes} gold from the village.')
        scene.gold += collected_taxes
