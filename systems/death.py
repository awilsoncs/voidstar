from components import Attributes, Entity
from components.seasonal_actors.rebuilder import Rebuilder
from components.coordinates import Coordinates
from components.corpse import Corpse
from components.drop_gold import DropGold
from components.house_structure import HouseStructure
from components.owner import Owner
from content import player, corpses
from content.gold import make_gold_nugget
from engine import palettes
from engine.constants import PLAYER_ID
from engine.core import log_debug


def run(scene):
    healths = [f for f in scene.cm.get(Attributes) if (f.hp <= 0)]
    for health in healths:

        owner = scene.cm.get_one(Owner, entity=health.entity)
        if owner:
            handle_owned_entity(scene, owner.owner)
        else:
            die(scene, health.entity)


def handle_owned_entity(scene, entity):
    # certainly a house for now...
    house_structures = [hs for hs in scene.cm.get(HouseStructure) if hs.house_id == entity]
    if house_structures:
        assert len(house_structures) == 1, "a house a may only have one structure"
        for house_structure in house_structures:
            for entity in house_structure.get_all():
                if scene.cm.get_one(Attributes, entity=entity):
                    die(scene, entity)
            scene.cm.add(Rebuilder(entity=house_structure.entity))


@log_debug(__name__)
def die(scene, entity):
    entity_obj = scene.cm.get_one(Entity, entity=entity)
    coords = scene.cm.get_one(Coordinates, entity=entity)
    corpse = scene.cm.get_one(Corpse, entity=entity)

    corpse_color = corpse.color if corpse else palettes.BLOOD

    x = coords.x
    y = coords.y
    scene.cm.add(*corpses.make_blood_splatter(5, x, y, corpse_color))

    gold = scene.cm.get_one(DropGold, entity=entity)
    if gold:
        scene.cm.add(*make_gold_nugget(x, y)[1])

    scene.cm.delete(entity)

    if entity == PLAYER_ID:
        scene.cm.add(*player.make_corpse(x, y)[1])
    else:
        scene.cm.add(*corpses.make_corpse(name=entity_obj.name, x=x, y=y, color=corpse_color)[1])
