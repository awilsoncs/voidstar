import logging
from dataclasses import dataclass

from components import Coordinates
from components.attack_start_listeners.attack_start_actor import AttackStartListener
from components.house_structure import HouseStructure
from components.relationships.residence import Residence
from components.tags.peasant_tag import PeasantTag


@dataclass
class MovePeasantsIn(AttackStartListener):
    """Move peasants into their homes when the attack begins."""
    def on_attack_start(self, scene):
        logging.info("Moving peasants into homes...")
        peasants = scene.cm.get(PeasantTag)
        for peasant in peasants:
            _move_peasant_home(scene, peasant)


def _move_peasant_home(scene, peasant) -> None:
    home_address = scene.cm.get_one(Residence, entity=peasant.entity)
    possible_homes = scene.cm.get(HouseStructure)
    correct_home = next(
        (hs for hs in possible_homes if hs.house_id == home_address.house_id),
        None
    )
    if correct_home:
        house_coords = scene.cm.get_one(Coordinates, entity=correct_home.entity)
        if house_coords:
            peasant_coords = scene.cm.get_one(Coordinates, entity=peasant.entity)
            if peasant_coords:
                peasant_coords.x = house_coords.x
                peasant_coords.y = house_coords.y
