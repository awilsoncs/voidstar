from components import Entity, Coordinates
from components.actors.hordeling_spawner import HordelingSpawner
from engine import core


def hordeling_spawner(x, y):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='hordeling spawner'),
            Coordinates(entity=entity_id, x=x, y=y),
            HordelingSpawner(entity=entity_id)
        ]
    )
