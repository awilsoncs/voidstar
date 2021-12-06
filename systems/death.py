from components import Attributes, Entity
from components.season_reset_listeners.rebuilder import Rebuilder
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
            _handle_rebuilder(scene, owner.owner)
        die(scene, health.entity)


def _handle_rebuilder(scene, entity):
    house_structures = scene.cm.get(HouseStructure, query=lambda hs: hs.house_id == entity)
    house_structure = house_structures[0] if house_structures else None
    if house_structure:
        scene.cm.add(Rebuilder(entity=house_structure.entity))
        house_structure.is_destroyed = True


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
