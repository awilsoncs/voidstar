from dataclasses import dataclass
from random import choice

from components import Coordinates
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from components.tags.peasant_tag import PeasantTag

moves = [
    (-2, -2), (0, -2), (2, -2),
    (-2, 0), (2, 0),
    (-2, 2), (0, 2), (2, 2)

]


@dataclass
class MovePeasantsOut(SeasonResetListener):
    """Move the peasants out of their houses at the end of each season."""
    def on_season_reset(self, scene):
        peasants = scene.cm.get(PeasantTag)
        for peasant in peasants:
            coords = scene.cm.get_one(Coordinates, entity=peasant.entity)
            if coords:
                direction = choice(moves)
                coords.x += direction[0]
                coords.y += direction[1]
