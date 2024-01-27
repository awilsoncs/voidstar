from components.actors.hordeling_spawner import HordelingSpawner
from engine import core
from engine.components.entity import Entity

description = "How did you even see this?"


def hordeling_spawner(waves):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='hordeling spawner', description=description),
            HordelingSpawner(entity=entity_id, waves=waves)
        ]
    )
