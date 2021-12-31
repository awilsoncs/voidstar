import logging
from dataclasses import dataclass

from components import Entity, Coordinates
from components.death_listeners.death_listener import DeathListener
from content import corpses
from engine import palettes


@dataclass
class Corpse(DeathListener):
    symbol: str = '%'
    color: tuple = palettes.BLOOD
    bg_color: tuple = palettes.BACKGROUND

    def on_die(self, scene):
        logging.info(f"Eid{self.entity}:Corpse spawned a corpse")
        entity_obj = scene.cm.get_one(Entity, entity=self.entity)
        coords = scene.cm.get_one(Coordinates, entity=self.entity)

        scene.cm.add(*corpses.make_blood_splatter(5, coords.x, coords.y, self.color))
        scene.cm.add(
            *corpses.make_corpse(
                name=entity_obj.name,
                symbol=self.symbol,
                x=coords.x,
                y=coords.y,
                color=self.color
            )[1]
        )
