from components import Entity, TimedActor
from components.actors.calendar_actor import CalendarTimedActor
from components.calendar import Calendar
from components.enums import ControlMode
from engine import core


def make_calendar():
    entity_id = core.get_id('calendar')
    return [
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='calendar'),
            Calendar(entity=entity_id),
            CalendarTimedActor(entity=entity_id)
        ]
    ]
