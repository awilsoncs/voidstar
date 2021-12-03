from components import Entity
from components.seasonal_actors.add_villager import AddVillager
from components.actors.calendar_actor import Calendar
from components.seasonal_actors.collect_taxes import CollectTaxes
from components.seasonal_actors.move_peasants_out import MovePeasantsOut
from components.seasonal_actors.reset_health import ResetHealth
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
            AddVillager(entity=entity_id),
            MovePeasantsOut(entity=entity_id)
        ]
    ]
