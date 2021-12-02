from dataclasses import dataclass
from typing import List

from components.actors.seasonal_actor import SeasonalActor
from components.tax_value import TaxValue


@dataclass
class CollectTaxes(SeasonalActor):
    def act(self, scene):
        taxes: List[TaxValue] = scene.cm.get(TaxValue)
        collected_taxes = sum(tax.value for tax in taxes)
        scene.popup_message(f'You collect {collected_taxes} gold from the village.')
        scene.gold += collected_taxes
