from dataclasses import dataclass

import content.corpses
import content.player_corpse
from components import Coordinates
from components.events.die_events import DeathListener
from content import corpses
from engine import palettes


@dataclass
class PlayerCorpse(DeathListener):
    symbol: str = '%'
    color: tuple = palettes.BLOOD
    bg_color: tuple = palettes.BACKGROUND

    def on_die(self, scene):
        self._log_info("spawned a corpse")
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        scene.cm.add(*corpses.make_blood_splatter(5, coords.x, coords.y, self.color))
        scene.cm.add(*content.player_corpse.make_player_corpse(x=coords.x, y=coords.y)[1])
