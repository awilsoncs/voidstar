from components import Entity
from components.actors.add_villager import AddVillager
from components.actors.calendar_actor import Calendar
from components.actors.collect_taxes import CollectTaxes
from components.actors.reset_health import ResetHealth
from engine import core


def make_calendar():
    entity_id = core.get_id('calendar')
    return [
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='calendar'),
            Calendar(entity=entity_id),
            ResetHealth(entity=entity_id),
            CollectTaxes(entity=entity_id),
            AddVillager(entity=entity_id)
        ]
    ]
