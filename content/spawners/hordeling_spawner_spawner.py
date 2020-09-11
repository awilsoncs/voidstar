from components import Entity
from components.actors.hordeling_spawner_spawner import HordelingSpawnerSpawner
from engine import core


def hordeling_spawner_spawner():
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='hordeling spawner spawner'),
            HordelingSpawnerSpawner(entity=entity_id)
        ]
    )
