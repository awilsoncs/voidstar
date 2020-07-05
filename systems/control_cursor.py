import tcod.event

from components import TimedActor, Coordinates, Entity
from components.cursor_result import CursorResult
from components.enums import Intention, ControlMode
from components.owner import Owner
from content.cursor import make_cursor
from engine import core
from systems.utilities import retract_intention, get_actors_with_intention, set_intention


def run(scene):
    _create_cursor(scene)
    _control_cursor(scene)
    _report_cursor_result(scene)
    _process_result(scene, _report_look)
    _process_result(scene, _report_target)
    _kill_cursor(scene)


def _create_cursor(scene):
    for actor in get_actors_with_intention(scene, Intention.ACTIVATE_CURSOR):
        actor.control_mode = None
        cursor_result = CursorResult(entity=actor.entity)
        scene.cm.add(cursor_result)

        coords = scene.cm.get_one(Coordinates, entity=actor.entity)
        cursor = make_cursor(scene.zone_id, coords.x, coords.y, actor.entity)
        scene.cm.add(*cursor[1])
        retract_intention(scene, actor.entity)


def _control_cursor(scene):
    for actor in [b for b in scene.cm.get(TimedActor) if b.control_mode is ControlMode.CURSOR]:
        key_event = core.get_key_event()
        if key_event:
            key_event = key_event.sym
            if key_event in KEY_ACTION_MAP:
                intention = KEY_ACTION_MAP[key_event]
                set_intention(scene, actor.entity, None, intention)


KEY_ACTION_MAP = {
    tcod.event.K_UP: Intention.STEP_NORTH,
    tcod.event.K_DOWN: Intention.STEP_SOUTH,
    tcod.event.K_RIGHT: Intention.STEP_EAST,
    tcod.event.K_LEFT: Intention.STEP_WEST,
    tcod.event.K_RETURN: Intention.REPORT_LOCATION,
    tcod.event.K_ESCAPE: Intention.KILL_CURSOR
}


def _report_cursor_result(scene):
    for actor in get_actors_with_intention(scene, Intention.REPORT_LOCATION):
        owner = scene.cm.get_one(Owner, entity=actor.entity).owner
        cursor_result = scene.cm.get_one(CursorResult, entity=owner)
        coords = scene.cm.get_one(Coordinates, entity=actor.entity)

        cursor_result.x = coords.x
        cursor_result.y = coords.y
        retract_intention(scene, actor.entity)


def _process_result(scene, fn):
    for result in scene.cm.get(CursorResult):
        if result.x is not None:
            x = result.x
            y = result.y

            fn(scene, x, y)
            result.x = None
            result.y = None


def _report_look(scene, x, y):
    objects = scene.cm.get(Coordinates)
    for object in objects:
        if object.x == x and object.y == y:
            object_name = scene.cm.get_one(Entity, entity=object.entity).name
            if object_name != 'cursor':
                scene.message(object_name)


def _report_target(scene, x, y):
    objects = scene.cm.get(Coordinates)
    for object in objects:
        if object.x == x and object.y == y:
            object_id = object_id
            if object_name != 'cursor':
                scene.message(object_name)


def _kill_cursor(scene):
    for actor in get_actors_with_intention(scene, Intention.KILL_CURSOR):
        owner = scene.cm.get_one(Owner, entity=actor.entity).owner
        scene.cm.delete(actor.entity)
        owner_actor = scene.cm.get_one(TimedActor, entity=owner)
        owner_actor.control_mode = ControlMode.PLAYER
