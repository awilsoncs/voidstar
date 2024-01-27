from components.season_reset_listeners.collect_taxes_for_king import CollectTaxesForKing
from components.season_reset_listeners.collect_taxes import CollectTaxes
from components.season_reset_listeners.extract_contract_fees import ExtractContractFees
from engine import core
from engine.components.entity import Entity


def make_tax_handler():
    entity_id = core.get_id('tax handler')
    return [
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='tax handler'),
            CollectTaxes(entity=entity_id),
            ExtractContractFees(entity=entity_id),
            CollectTaxesForKing(entity=entity_id)
        ]
    ]
