from dataclasses import dataclass
from random import choice

from components import Attributes, Appearance
from components.abilities.masonry_ability import MasonryAbility
from components.death_listeners.npc_corpse import Corpse
from components.house_structure import HouseStructure
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from engine import palettes


@dataclass
class UpgradeHouse(SeasonResetListener):
    def on_season_reset(self, scene):
        masonry_ability = scene.cm.get_one(MasonryAbility, entity=scene.player)
        max_upgrade = 2 if masonry_ability else 1

        house_structures = scene.cm.get(
            HouseStructure,
            query=lambda hs: hs.upgrade_level != max_upgrade and not hs.is_destroyed
        )

        if not house_structures:
            # Everything is upgraded.
            return
        else:
            house_structure = choice(house_structures)

        upgrade = [palettes.WOOD, palettes.STONE][house_structure.upgrade_level]

        walls = house_structure.get_all()
        for wall in walls:
            attributes = scene.cm.get_one(Attributes, entity=wall)
            attributes.hp = attributes.max_hp = (attributes.max_hp + 20)

            appearance = scene.cm.get_one(Appearance, entity=wall)
            appearance.color = upgrade

            corpse_def = scene.cm.get_one(Corpse, entity=wall)
            corpse_def.color = upgrade

        house_structure.upgrade_level += 1




