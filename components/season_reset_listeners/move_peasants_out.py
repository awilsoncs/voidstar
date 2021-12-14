from dataclasses import dataclass
from random import choice

from components import Coordinates
from components.game_start_listeners.game_start_listener import GameStartListener
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from components.tags.peasant_tag import PeasantTag

moves = [
    (-2, -2), (0, -2), (2, -2),
    (-2, 0), (2, 0),
    (-2, 2), (0, 2), (2, 2)

]


def _move_peasants_out(scene):
    peasants = scene.cm.get(PeasantTag)
    for peasant in peasants:
        coords = scene.cm.get_one(Coordinates, entity=peasant.entity)
        if coords:
            direction = choice(moves)
            coords.x += direction[0]
            coords.y += direction[1]


@dataclass
class MovePeasantsOut(SeasonResetListener, GameStartListener):
    """Move the peasants out of their houses."""
    def on_season_reset(self, scene):
        _move_peasants_out(scene)

    def on_game_start(self, scene):
        _move_peasants_out(scene)
