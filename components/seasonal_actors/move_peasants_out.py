from dataclasses import dataclass
from random import choice

from components import Coordinates
from components.seasonal_actors.seasonal_actor import SeasonalActor
from components.tags.peasant_tag import PeasantTag

moves = [
    (-2, -2), (0, -2), (2, -2),
    (-2, 0), (2, 0),
    (-2, 2), (0, 2), (2, 2)

]


@dataclass
class MovePeasantsOut(SeasonalActor):
    """Move the peasants out of their houses at the end of each season."""
    def act(self, scene):
        peasants = scene.cm.get(PeasantTag)
        for peasant in peasants:
            coords = scene.cm.get_one(Coordinates, entity=peasant.entity)
            if coords:
                direction = choice(moves)
                coords.x += direction[0]
                coords.y += direction[1]
