from components import Attributes, Entity
from components.coordinates import Coordinates
from content import player, corpses
from engine.constants import PLAYER_ID
from engine.core import log_debug


def run(scene):
    healths = [f for f in scene.cm.get(Attributes) if (f.hp <= 0)]
    for health in healths:
        die(scene, health.entity)


@log_debug(__name__)
def die(scene, entity):
    entity_obj = scene.cm.get_one(Entity, entity=entity)
    coords = scene.cm.get_one(Coordinates, entity=entity)
    if entity == PLAYER_ID:
        scene.cm.add(*player.make_corpse(coords.x, coords.y)[1])
    else:
        scene.cm.add(*corpses.make_corpse(name=entity_obj.name, x=coords.x, y=coords.y)[1])
    scene.cm.add(*corpses.make_blood_splatter(5, coords.x, coords.y))
    scene.cm.delete(entity)
