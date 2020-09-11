from components import Attributes, Entity
from components.coordinates import Coordinates
from components.drop_gold import DropGold
from content import player, corpses
from content.gold import make_gold_nugget
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
    x = coords.x
    y = coords.y
    scene.cm.add(*corpses.make_blood_splatter(5, x, y))

    gold = scene.cm.get_one(DropGold, entity=entity)
    if gold:
        scene.cm.add(*make_gold_nugget(x, y)[1])

    scene.cm.delete(entity)

    if entity == PLAYER_ID:
        scene.cm.add(*player.make_corpse(x, y)[1])
    else:
        scene.cm.add(*corpses.make_corpse(name=entity_obj.name, x=x, y=y)[1])
