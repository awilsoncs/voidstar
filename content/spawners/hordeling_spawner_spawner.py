from components import Entity
from components.actors.hordeling_spawner_spawner import HordelingSpawnerSpawner
from engine import core

description = "How did you even see this?"


def hordeling_spawner_spawner(waves):
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='hordeling spawner spawner', description=description),
            HordelingSpawnerSpawner(entity=entity_id, waves=waves)
        ]
    )
